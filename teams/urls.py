from django.conf.urls import url
from .views import register, checkusername,example
urlpatterns = [
    url(r'^$', example,name='example'),
    url(r'register/$', register, name = 'register'),
    url(r'checkusername/$', checkusername, name = 'checkusername')
]
