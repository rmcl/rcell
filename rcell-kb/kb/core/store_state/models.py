from django.db import models
import reference.models as reference_models
import molecule.models as molecule_models

class StateGroup(reference_models.ReferenceMixin):
    name = models.CharField(max_length=150, unique=True)
    
class MoleculeConcentration(reference_models.ReferenceMixin):
    
    molecule = models.ForeignKey(molecule_models.Molecule)
    concentration = models.FloatField()