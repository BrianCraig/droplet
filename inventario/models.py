from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
# Create your models here.

class Articulo(models.Model):
    usuario = models.ForeignKey(User)
    titulo = models.CharField(max_length=200,blank=True)
    descripcion = models.CharField(max_length=1000,blank=True)
    stock = models.IntegerField(default=0)
    stock_warn = models.IntegerField(default=0)
    vistas = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def agregarStock(self,cantidad):
        self.stock += cantidad
        self.save()



class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo','descripcion','stock','stock_warn']