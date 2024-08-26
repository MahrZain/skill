from django.contrib import admin
from .models import crudUser

# Register your models here.

class crudAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'slug']  
    prepopulated_fields = {'slug': ('name',)}     
admin.site.register(crudUser, crudAdmin)

