from django.db import models

# Create your models here.
class Menu(models.Model):
    titulo = models.CharField(max_length = 140)
    enlace = models.CharField(max_length = 140)
        
    def __unicode__(self):
        return self.titulo