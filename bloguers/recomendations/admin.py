from django.contrib import admin
from .models import Recomendation, Category, State

# Register your models here.
class RecomendationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

admin.site.register(Recomendation,RecomendationAdmin)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

admin.site.register(Category,CategoryAdmin)

class StateyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

admin.site.register(State,StateyAdmin)