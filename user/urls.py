from django.contrib import admin
from django.urls import path
from . import views
from user.views import index, RegisterView, LoginView

urlpatterns = [
    path('',views.index),
    path('join/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]