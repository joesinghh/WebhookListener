from django.urls import path
from . import views
urlpatterns = [
        path("call/",views.call),
    ]

