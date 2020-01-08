from django.db import models

# Create your models here.
class Social(models.Model):
    name = models.CharField(verbose_name='Red social', max_length=15)
    link = models.URLField(verbose_name='URL', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Enlace'
        verbose_name_plural = 'Enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name