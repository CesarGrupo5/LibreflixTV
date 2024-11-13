from django.contrib import admin
from LibreflixApp.models import Obra, Filme, Serie, Episodio, Favoritados, ContinuarAssistindo

admin.site.register(Obra)
admin.site.register(Filme)
admin.site.register(Serie)
admin.site.register(Episodio)
admin.site.register(Favoritados)
admin.site.register(ContinuarAssistindo)