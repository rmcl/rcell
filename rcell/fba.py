import rcell.core as core
import rcell.kb.reactions as reactions

#class StoichiometryMatrixState(core.StateGroup):
#    def __init__(self):
#        self.size = 

class ReactionFBA(core.Simulation):
    
    def __init__(self, compartment, metabolites, time_step=1.0):
        self.set_time_step(time_step)
        self.add_structure('compartment', compartment)
        
        participants = reactions.reactions_participants(metabolites.metabolites)
        print reactions.build_stoich_matrix(participants)
        
        
    def update(self, clock, states):
        
        print clock, states
        
        return states