import sys
import xmlrpclib
import numpy as np

def reactions_participants(participants):
    '''
    Fetch reactions for list of given participants.
    '''
    srv = xmlrpclib.ServerProxy("http://localhost:8001/rpc")

    return srv.reaction.get_participants(["O2"])


def build_stoich_matrix(reaction_participants):
    '''
    Build a stoichiometry matrix from a dictionary of reactions. The matrix
    is nxm where n is the number of molecules and m is the number of reactions.
    
    Reference
    ---------
    * http://en.wikipedia.org/wiki/Stoichiometry#Stoichiometry_matrix
    
    Parameters
    ---------
    :params reaction_participants: A dictionary of reactions names to their
        component molecular parts and their coefficients.
        ex. {'R1': [(1, 'NADH'), (-1, 'O2')]}
    :return: A nxm numpy array representing the stoichiometry matrix. 
    '''
    reactions = {}
    participants = {}
    
    # Count participants
    participant_count = 0
    for reaction_name, particips in reaction_participants.iteritems():
        for coefficient, participant in particips:
            participant_count += 1
    
    dim = (participant_count, len(reaction_participants.keys()))
    stoich = np.zeros(dim)
    
    # Iterate through the returned reactions
    for reaction_name, particips in reaction_participants.iteritems():
        if reaction_name not in reactions:
            reactions[reaction_name] = len(reactions)
        
        for coefficient, p in particips:
            # If we have never encountered this molecule before. Assign it
            # the next available participant_id
            if p not in participants:
                participants[p] = len(participants)
            
            stoich[participants[p], reactions[reaction_name]] = coefficient
     
    return stoich