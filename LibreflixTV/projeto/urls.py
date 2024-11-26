from django.contrib import admin
from django.urls import path

from LibreflixApp.views import HomeView, PageView, FavoritosView, ObraView, CatalogoView, GeneroView, SairView, PesquisaView, LoginView, RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('', PageView.as_view(), name='page'),
    path('favoritos/', FavoritosView.as_view(), name='favoritos'),
    path('obra/<int:id>/', ObraView.as_view(), name='obra_info'),
    path('generos/', CatalogoView.as_view(), name='generos'),
    path('generos/<str:genero>/', GeneroView.as_view(), name='genero_info'),
    path('sair/', SairView.as_view(), name='sair'),
    path('pesquisa/<str:titulo>/', PesquisaView.as_view(), name='pesquisa'),
    path('pesquisa/', PesquisaView.as_view(), name='pesquisa_vazia'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
]