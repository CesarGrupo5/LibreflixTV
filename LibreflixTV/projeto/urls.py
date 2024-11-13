from django.contrib import admin
from django.urls import path

from LibreflixApp.views import HomeView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('', LoginView.as_view(), name='login'),
]
