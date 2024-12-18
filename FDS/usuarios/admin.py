from django.contrib import admin
from .models import Materia
from django.contrib import admin
from .models import Usuario
from .models import Documento
from .models import Solicitacao
from .models import Evento, AvisoAcademico, Horario

admin.site.register(Usuario)
admin.site.register(Documento)
admin.site.register(Solicitacao)
admin.site.register(Evento)
admin.site.register(AvisoAcademico)
admin.site.register(Horario)

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')  # Exibe o nome e a descrição no admin
    search_fields = ('nome',)  # Adiciona um campo de busca por nome