from django.db import models

import reference.models as reference_models

class Molecule(reference_models.ReferenceMixin):
    acronym = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    traditional_name = models.TextField(blank=True, default='', verbose_name='Traditional name')
    iupac_name = models.TextField(blank=True, default='', verbose_name='IUPAC name')

    empirical_formula = models.TextField()
    
    def __unicode__(self):
        return self.acronym