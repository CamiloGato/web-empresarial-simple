from django.contrib import admin
from .models import Social

# Register your models here.
class SocialkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

admin.site.register(Social, SocialkAdmin)