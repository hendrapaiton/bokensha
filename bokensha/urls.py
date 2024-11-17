from django.contrib import admin
from django.urls import path

from apps.landing.views import LoginView, SuccessView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_page'),
    path('success/', SuccessView.as_view(), name='success'),
    path('admin/', admin.site.urls),
]
