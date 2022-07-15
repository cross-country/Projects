from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Опис')
    price = models.FloatField(null=True, blank=True, verbose_name='Ціна')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубліковано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    class Meta:
        verbose_name_plural = "Об'яви"
        verbose_name = "Об'ява"
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Назва')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
