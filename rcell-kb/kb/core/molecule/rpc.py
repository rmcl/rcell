from django.forms.models import model_to_dict
from rpc4django import rpcmethod

import molecule.models as molecule_models

@rpcmethod(name='molecule.ping', signature=[])
def ping():
    return 'PONG'
    

@rpcmethod(name='molecule.list', signature=[])
def list():
    molecules = molecule_models.Molecule.objects.all()
    x = [model_to_dict(molecule) for molecule in molecules]

    return x