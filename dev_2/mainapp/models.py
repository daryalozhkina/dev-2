from django.db import models


class Noun(models.Model):
    text = models.TextField(verbose_name='Существительное')


class Meta:
    verbose_name = 'Существительное'
    verbose_name_plural = 'Существительные'
