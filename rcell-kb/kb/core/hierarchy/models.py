from django.db import models

class Entry(models.Model):
    eid = SlugField(max_length=150, verbose_name='Entry Id', unique=True)
    
    references = ManyToManyField('Reference', blank=True, null=True,
        related_name='referenced_entries', verbose_name='References')