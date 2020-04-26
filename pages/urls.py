from django.urls import path
from .views import home, send_mail

urlpatterns = [
    path('', home, name='home'),
    path('sendmail', send_mail, name='sendmail'),
]
