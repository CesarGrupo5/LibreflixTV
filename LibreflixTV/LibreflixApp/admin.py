from django.contrib import admin
from LibreflixApp.models import Obra, Filme, Serie, Episodio, Favoritados, ContinuarAssistindo

class ObraAdmin(admin.ModelAdmin):
    list_display = ('titulo','genero','dataLancamento', 'diretor', 'isPopular', 'isRecente', 'isDestaque')
    actions = ['make_popular', 'make_recente', 'make_destaque', 'make_nao_popular', 'make_nao_recente', 'make_nao_destaque']

    def make_popular(self, request, queryset):
        queryset.update(isPopular=True)
        self.short_description = "Marcar como popular"

    def make_recente(self, request, queryset):
        queryset.update(isRecente=True)
        self.short_description = "Marcar como recente"

    def make_destaque(self, request, queryset):
        queryset.update(isDestaque=True)
        self.short_description = "Marcar como destaque"
    
    def make_nao_popular(self, request, queryset):
        queryset.update(isPopular=False)
        self.short_description = "Desmarcar como popular"

    def make_nao_recente(self, request, queryset):
        queryset.update(isRecente=False)
        self.short_description = "Desmarcar como recente"

    def make_nao_destaque(self, request, queryset):
        queryset.update(isDestaque=False)
        self.short_description = "Desmarcar como destaque"

class FilmeAdmin(ObraAdmin):
    list_display = ('titulo','genero','dataLancamento', 'duracao','diretor', 'isPopular', 'isRecente', 'isDestaque')

class SerieAdmin(ObraAdmin):
    list_display = ('titulo','genero','dataLancamento', 'qntEpisodios','diretor', 'isPopular', 'isRecente', 'isDestaque')

class EpisodioAdmin(admin.ModelAdmin):
    list_display = ('titulo','descricao','obra','duracao')

class CommonDisplay(admin.ModelAdmin):
    list_display = ('obra','usuario')

admin.site.register(Obra, ObraAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Episodio, EpisodioAdmin)
admin.site.register(Favoritados, CommonDisplay)
admin.site.register(ContinuarAssistindo, CommonDisplay)

