from django.shortcuts import render, redirect
from django.views import View

from LibreflixApp.models import Obra, ContinuarAssistindo

class HomeView(View):
    def get(self, request):
        destaques = Obra.objects.filter(isDestaque=True).all()
        longas = Obra.objects.filter(isPopular=True).all()
        recentes = Obra.objects.filter(isRecente=True).all()
        continuar = ContinuarAssistindo.objects.filter(usuario=request.user).all()

        context = { 'destaques': destaques, 'longas': longas, 'recentes': recentes, 'continuar': continuar }

        return render(request, 'home.html', context)
    
class LoginView(View):
    def get(self, request):

        # se já estiver autenticado, redirecionar para home
        if(request.user.is_authenticated):
            return redirect('home')

        return render(request, 'login.html')
    