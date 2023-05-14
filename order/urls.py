from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'payment'

urlpatterns = [
    path('', views.kakaoPay),
    path('paySuccess/', views.paySuccess),
    path('kakaoPayLogic/', views.kakaoPayLogic),
    path('payFail/', views.payFail),
    path('payCancle/', views.payCancle),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)