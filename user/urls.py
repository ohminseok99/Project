from django.contrib import admin
from django.urls import path
from . import views
from user.views import index, RegisterView, LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index),
    path('join/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', views.logoutview),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


