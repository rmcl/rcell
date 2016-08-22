import xmlrpclib
import numpy as np
import pprint


def get_reactions_with_participants(participants):
    """Fetch reactions for list of given participants."""
    kb_api = xmlrpclib.ServerProxy("http://localhost:8000/rpc")

    print 'PARTICIPANTS', participants
    reactions = kb_api.reaction.get_reactions_with_participants(participants)
    pprint.pprint(reactions)
    return reactions


def build_stoichiometry_matrix(reactions_list_inp):
    """
    Build a stoichiometry matrix from a dictionary of reactions.

    The matrix is nxm where n is the number of molecules and m is the number of reactions.

    Reference
    ---------
    * http://en.wikipedia.org/wiki/Stoichiometry#Stoichiometry_matrix

    Parameters
    ---------
    :params reactions: A dictionary of reactions names to their
        component molecular parts and their coefficients.
        ex. {'R1': [(1, 'NADH'), (-1, 'O2')]}
    :return: A nxm numpy array representing the stoichiometry matrix.
    """
    reactions_index = {}
    participant_index = {}

    # Create indexes for reaction participants
    for reaction_name, particips in reactions_list_inp.iteritems():
        for coefficient, participant in particips:
            # If we have never encountered this molecule before. Assign it
            # the next available participant_id
            if participant not in participant_index:
                participant_index[participant] = len(participant_index)

    dim = (len(participant_index), len(reactions_list_inp.keys()))
    stoich_matrix = np.zeros(dim)

    # Iterate through the returned reactions and build up stoichiometry matrix
    for reaction_name, particips in reactions_list_inp.iteritems():
        if reaction_name not in reactions_index:
            reactions_index[reaction_name] = len(reactions_index)

        for coefficient, p in particips:
            index = (participant_index[p], reactions_index[reaction_name])
            stoich_matrix[index] += coefficient

    return {
        'N': stoich_matrix,
        'reactions': reactions_index,
        'participants': participant_index
    }
