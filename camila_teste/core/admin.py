from django.contrib import admin

from .models import Motorista, Passageiro

# Register your models here.
@admin.register(Motorista)
class MotoristaAdmin(admin.ModelAdmin):
    pass

@admin.register(Passageiro)
class PassageiroAdmin(admin.ModelAdmin):
    pass