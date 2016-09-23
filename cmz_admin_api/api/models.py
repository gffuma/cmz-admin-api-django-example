from __future__ import unicode_literals

from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    date = models.DateField()
