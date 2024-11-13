from django.shortcuts import render, redirect
from django.views import View

from LibreflixApp.models import Obra, ContinuarAssistindo, Favoritados, Filme, Serie, Episodio

class HomeView(View):
    def get(self, request):
        destaques = Obra.objects.filter(isDestaque=True).all()
        longas = Obra.objects.filter(isPopular=True).all()
        recentes = Obra.objects.filter(isRecente=True).all()
        continuar = ContinuarAssistindo.objects.filter(usuario=request.user).all()

        context = { 'destaques': destaques, 'longas': longas, 'recentes': recentes, 'continuar': continuar }

        return render(request, 'home.html', context)
    
class PageView(View):
    def get(self, request):

        # se já estiver autenticado, redirecionar para home
        if(request.user.is_authenticated):
            return redirect('home')

        return render(request, 'page.html')
    
class FavoritosView(View):
    def get(self, request):
        context = {'favoritos': Favoritados.objects.filter(usuario=request.user).all()}
        return render(request, 'favoritos.html', context)
    
class ObraView(View):
    def get(self, request, id):

        # Verifica se é um filme ou uma serie
        if(Filme.objects.filter(id=id).exists()):
            obra = Filme.objects.get(id=id)
            return render(request, 'obraFilme.html', {'obra': obra})

        elif(Serie.objects.filter(id=id).exists()):
            obra = Serie.objects.get(id=id)
            episodios = Episodio.objects.filter(obra=obra).all()
            return render(request, 'obraSerie.html', {'obra': obra, 'episodios': episodios})