from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField('nome', max_length=100)
    price = models.DecimalField('preço', max_digits=10, decimal_places=2)
    description = models.TextField('descrição', blank=True, null=True)
    image = models.ImageField('imagem do produto', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        ordering = ['name', ]
