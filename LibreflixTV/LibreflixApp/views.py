from django.shortcuts import render, redirect
from django.contrib.auth import logout as lg
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.db.models import Avg

from LibreflixApp.models import Obra, ContinuarAssistindo, Favoritados, Filme, Serie, Episodio, Avaliacao
from LibreflixApp.forms import CustomUserCreationForm, CustomAuthenticationForm  
class RegistrationView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'registration.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Email ou senha incorretos.')
        return render(request, 'login.html', {'form': form})
        
class HomeView(View):
    def get(self, request):
        if(request.user.is_authenticated == False):
            return redirect('page')

        destaques = Obra.objects.filter(isDestaque=True).all()
        longas = Obra.objects.filter(isPopular=True).all()
        recentes = Obra.objects.filter(isRecente=True).all()
        continuar = ContinuarAssistindo.objects.filter(usuario=request.user).all()
        destacado = Obra.objects.filter(isDestaque=True).first()
        
        context = { 'destaques': destaques, 'longas': longas, 'recentes': recentes, 'continuar': continuar, 'destacado': destacado }
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
        if Filme.objects.filter(id=id).exists():
            obra = Filme.objects.get(id=id)
            isFavorito = ObraView.buscarFavorito(request.user, obra)
            avaliacao_usuario = ObraView.getAvaliacao(request.user, obra)
            media_avaliacoes = ObraView.getMediaAvaliacoes(obra)

            if avaliacao_usuario:
                nota_usuario = avaliacao_usuario.estrelas
            else :
                nota_usuario = 0

            context = {
                'obra': obra,
                'isFavorito': isFavorito,
                'avaliacao_usuario': avaliacao_usuario.estrelas if avaliacao_usuario else None,
                'nota_usuario': nota_usuario,
                'media_avaliacoes': media_avaliacoes,
            }
            return render(request, 'obraFilme.html', context)

        elif Serie.objects.filter(id=id).exists():
            obra = Serie.objects.get(id=id)
            episodios = ObraView.getEpisodios(obra)
            isFavorito = ObraView.buscarFavorito(request.user, obra)
            avaliacao_usuario = ObraView.getAvaliacao(request.user, obra)
            media_avaliacoes = ObraView.getMediaAvaliacoes(obra)

            if avaliacao_usuario:
                nota_usuario = avaliacao_usuario.estrelas
            else :
                nota_usuario = 0

            context = {
                'obra': obra,
                'episodios': episodios,
                'isFavorito': isFavorito,
                'avaliacao_usuario': avaliacao_usuario.estrelas,
                'nota_usuario': nota_usuario,
                'media_avaliacoes': media_avaliacoes,
            }
            return render(request, 'obraSerie.html', context)

    def post(self, request, id):
        if request.POST.get('starFavoritar'):
            ObraView.favoritar(request, id)
            return redirect('obra_info', id)

        if request.POST.get('starRemover'):
            ObraView.removerFavorito(request, id)
            return redirect('obra_info', id)

        obra = None
        if Filme.objects.filter(id=id).exists():
            obra = Filme.objects.get(id=id)
        elif Serie.objects.filter(id=id).exists():
            obra = Serie.objects.get(id=id)

        if obra is None:
            return redirect('obra_info', id)

        estrelas = request.POST.get('nota')
        if estrelas and estrelas.isdigit():
            estrelas = int(estrelas)
            if 1 <= estrelas <= 5:  
                Avaliacao.objects.update_or_create(
                    obra=obra,
                    usuario=request.user,
                    defaults={'estrelas': estrelas},
                )

        return redirect('obra_info', id)
    
    def getEpisodios(obra):
        return Episodio.objects.filter(obra=obra).all()
    
    def getAvaliacao(user, obra):
        return Avaliacao.objects.filter(obra=obra).filter(usuario=user).first()
    
    def getMediaAvaliacoes(obra):
        media =  Avaliacao.objects.filter(obra=obra).aggregate(Avg('estrelas'))['estrelas__avg']
        media = round(media, 1) if media else "0.0"
        return media

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

class PesquisaView(View):
    def get(self, request, titulo = None):
        if titulo is not None:
            obras = PesquisaView.filterObras(titulo)

        context = {'obras': obras}
        return render(request, "pesquisa.html", context)
    
    def post(self, request):
        titulo = request.POST.get('titulo')
        return redirect('pesquisa', titulo)
    
    def filterObras(titulo):
        todasObras = Obra.objects.all()
        obras = []

        for obra in todasObras:
            if obra.titulo.lower().startswith(titulo.lower()):
                obras.append(obra)

        if obras == []:
            return None
        else:
            return obras