from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
    img = models.ImageField('product/', blank=True, null=True)
    category = models.ForeignKey('catalog.Category', on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
