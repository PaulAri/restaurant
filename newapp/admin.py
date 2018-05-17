from django.contrib import admin

# Register your models here.
from newapp.models import Produs

class ProdusAdmin(admin.ModelAdmin):
    list_display = ["title", "pret", "cantitate"]
    list_filter = ["title"]
    search_fields = ["title", "pret"]

admin.site.register(Produs, ProdusAdmin)