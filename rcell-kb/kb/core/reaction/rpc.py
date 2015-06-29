from django.forms.models import model_to_dict
from rpc4django import rpcmethod

import reaction.models as reaction_models
import molecule.models as molecule_models

@rpcmethod(name='reaction.list', signature=[dict])
def list():
    reactions = reaction_models.Reaction.objects.all()
    x = [model_to_dict(reaction) for reaction in reactions]

    return x

@rpcmethod(name='reaction.get_participants', signature=[list])
def get_participants(participants):
    
    print participants
    
    molecules = molecule_models.Molecule.objects.filter(acronym__in=participants)

    # Todo(rmcl): Yes this should be a join.
    reactions_participants = reaction_models.ReactionParticipant.objects.filter(molecule__in=molecules)
    reactions_participants = map(lambda rp: rp.reaction, reactions_participants)
    all_reaction_participants = reaction_models.ReactionParticipant.objects.filter(reaction__in=reactions_participants)

    reactions = {}
    for rp in all_reaction_participants:
        try:
            reactions[rp.reaction.name].append((rp.coefficient, rp.molecule.acronym))
        except KeyError:
            reactions[rp.reaction.name] = [(rp.coefficient, rp.molecule.acronym)]

    return reactions
    
@rpcmethod(name='reaction.get', signature=[int])
def get(reaction_id):
    reaction = reaction_models.Reaction.objects.get(pk=reaction_id)
    r = model_to_dict(reaction)
    r.update({
        'participants': [model_to_dict(p) for p in reaction.participants]
    })
    return r