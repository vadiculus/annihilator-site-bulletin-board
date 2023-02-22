from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import login
from .models import User
from .forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .utilites import signer
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import send_activation_email_task

class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO , 'Вы успешно зерегестрировались! Теперь можете войти в аккаунт')
        self.object = form.save()
        return HttpResponseRedirect(reverse('accounts:activation_warning', args=[signer.sign(self.object.username)]))

class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    model = User
    success_url = reverse_lazy('posts:index')

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO , 'Вы вошли ваккаунт!')
        return super().form_valid(form)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('posts:index'))

def my_profile_view(request):
    if request.user.profile:
        return render(request, 'accounts/no_profile')

def profile_view(request, username):
    user = User.objects.prefetch_related('products').get(username=username)
    return render(request, 'accounts/profile.html', {'profile_user':user})

def activation_user_view(request, sign):
    user = User.objects.get(username=signer.unsign(sign))
    user.is_active = True
    user.save()
    return render(request,'accounts/success_activation.html', {})

def activation_warning_view(request, sign):
    return render(request, 'accounts/activation_warning.html', {'sign':sign})

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('posts:index')

def resend_activation(request, sign):
    user = User.objects.get(username=signer.unsign(sign))
    send_activation_email_task.delay(user.email, user.username)
    return HttpResponseRedirect(reverse('accounts:activation_warning', args=[sign]))

