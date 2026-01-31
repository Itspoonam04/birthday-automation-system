from django.urls import path
from .views import home, register_customer, unsubscribe

urlpatterns = [
    path("", home, name="home"),
    path("api/register/", register_customer, name="register_customer"),
    path("unsubscribe/<uuid:token>/", unsubscribe, name="unsubscribe"),
]

