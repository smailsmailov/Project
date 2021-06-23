from django.urls import path

from .views import SignIpFirst

urlpatterns = [
    path( 'signup/' , SignIpFirst , name='signup' ) ,
]