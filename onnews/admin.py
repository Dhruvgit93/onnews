from django.contrib import admin
from .models import blogs

@admin.register(blogs)
class blogadminview(admin.ModelAdmin):
    list_display=("pk","title")
    

