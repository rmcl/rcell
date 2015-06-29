from django.db import models

import reference.models as reference_models
import molecule.models as molecule_models

class Reaction(reference_models.ReferenceMixin):
    name = models.CharField(max_length=150, unique=True)
    
    def _participants(self):
        '''
        List this reaction's participating molecules.
        '''
        return ReactionParticipant.objects.filter(reaction=self)
    participants = property(_participants)
    
    def __unicode__(self):
        return self.name
    
class ReactionParticipant(reference_models.ReferenceMixin):
    reaction = models.ForeignKey(Reaction)
    coefficient = models.FloatField(verbose_name='Coefficient')
    molecule = models.ForeignKey(molecule_models.Molecule)