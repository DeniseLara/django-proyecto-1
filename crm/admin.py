from django.contrib import admin
from .models import Company, Client, Interaction

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'commercial')
    search_fields = ('name', 'email', 'company__name')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    search_fields = ('client__name',)