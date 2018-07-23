from django.conf.urls import url
from .views import register, checkusername
urlpatterns = [
    url(r'register/$', register, name = 'register'),
    url(r'checkusername/$', checkusername, name = 'checkusername')
]