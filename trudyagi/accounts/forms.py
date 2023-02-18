from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .apps import register_signal

class RegistrationForm(UserCreationForm):

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
            print('Register')
        register_signal.send(RegistrationForm, instance=user)
        return user


    class Meta:
        model = User
        fields = ['username','first_name','last_name','icon', 'email', 'password1', 'password2']