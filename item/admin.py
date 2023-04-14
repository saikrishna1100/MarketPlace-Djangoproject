from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryView(admin.ModelAdmin):
    
    list_display=["id","name"]
    search_fields=["id","name"]
admin.site.register(Category,CategoryView)