from django.contrib import admin

from .models import Motorista, Passageiro, Corrida

# Register your models here.


@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    pass


@admin.register(Passageiro)
class PassageiroAdmin(admin.ModelAdmin):
    pass


@admin.register(Corrida)
class CorridaAdmin(admin.ModelAdmin):
    pass
