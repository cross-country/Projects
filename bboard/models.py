from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Опис')
    price = models.FloatField(null=True, blank=True, verbose_name='Ціна')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубліковано')

    class Meta:
        verbose_name_plural = "Об'яви"
        verbose_name = "Об'ява"
        ordering = ['-published']

