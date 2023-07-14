from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, unique=True)
    desc = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
