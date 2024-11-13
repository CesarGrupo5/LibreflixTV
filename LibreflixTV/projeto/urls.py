from django.contrib import admin
from django.urls import path

from LibreflixApp.views import HomeView, PageView, FavoritosView, ObraView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('', PageView.as_view(), name='page'),
    path('favoritos/', FavoritosView.as_view(), name='favoritos'),
    path('obra/<int:id>/', ObraView.as_view(), name='obra_info'),
]
