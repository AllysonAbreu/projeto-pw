from django.contrib import admin
from .models import Receita


class LitandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'publicada')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 5


admin.site.register(Receita, LitandoReceitas)
