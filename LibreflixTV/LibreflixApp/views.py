from django.shortcuts import render, redirect
from django.contrib.auth import logout as lg
from django.views import View

from LibreflixApp.models import Obra, ContinuarAssistindo, Favoritados, Filme, Serie, Episodio

class HomeView(View):
    def get(self, request):
        if(request.user.is_authenticated == False):
            return redirect('page')

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
            isFavorito = ObraView.buscarFavorito(request.user, obra)

            context = {'obra': obra, 'isFavorito': isFavorito}
            return render(request, 'obraFilme.html', context)

        elif(Serie.objects.filter(id=id).exists()):
            obra = Serie.objects.get(id=id)
            episodios = Episodio.objects.filter(obra=obra).all()
            isFavorito = ObraView.buscarFavorito(request.user, obra)

            context = {'obra': obra, 'episodios': episodios, 'isFavorito': isFavorito}
            return render(request, 'obraSerie.html', context)
        
    def post(self, request, id):
        if(request.POST.get('starFavoritar')):
            ObraView.favoritar(request, id)
            return redirect('obra_info', id)
        
        if(request.POST.get('starRemover')):
            ObraView.removerFavorito(request, id)
            return redirect('obra_info', id)

    def favoritar(request, id):
        f = Favoritados()
        f.usuario = request.user
        f.obra = Obra.objects.filter(id=id).first()

        if(ObraView.buscarFavorito(request.user, f.obra) == False):
            f.save()

    def removerFavorito(request, id):
        if(ObraView.buscarFavorito(request.user, Obra.objects.filter(id=id).first()) == True):
            f = Favoritados.objects.filter(usuario=request.user, obra=Obra.objects.filter(id=id).first()).first()
            f.delete()
    
    def buscarFavorito(user, obra):
        if(Favoritados.objects.filter(usuario=user, obra=obra).exists()):
            return True
        else:
            return False

class CatalogoView(View):   
    def get(self, request):
        return render(request, 'catalogo.html')

class GeneroView(View):
    def get(self, request, genero):
        obras = Obra.objects.filter(genero=genero).all()

        context = {'obras': obras, 'genero': genero}
        return render(request, 'genero.html', context)
    
class SairView(View):
    def get(self, request):
        lg(request)
        return redirect('page')