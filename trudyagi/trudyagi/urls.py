from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace='chat')),
    path('', include('posts.urls', namespace='posts')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('silk/', include('silk.urls', namespace='silk')),
    path('cart/', include('cart.urls', namespace='cart')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/', serve, {'document_root': settings.STATIC_ROOT})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'trudyagi.views.handler404'
handler403 = 'trudyagi.views.handler403'
handler500 = 'trudyagi.views.handler500'
