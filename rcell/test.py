import rcell.core as core
import fba
from membrane_transport import MembraneTransport

class Metabolites(core.StateGroup):
    '''
    Store the metabolite concentrations in a compartment.
    '''
    
    def __init__(self):
        self.size = 3
        self.metabolites = ['ATP', 'NADH', 'O2']
        self._initial = {}
        
    def initial(self, metabolite_name, concentration):
        self._initial[metabolite_name] = concentration
        
    def build(self, start_pos):
        '''
        Setup the state group.
        '''

class ExtracellularEnvironment(core.Compartment):
    def __init__(self):
        m = Metabolites()
        m.initial('O2', 12)
        
        self.add_states('metabolites', )
        
        
    
class EcoliCell(core.Compartment):

    def __init__(self):
        m = Metabolites()
        
        m.initial('ATP', 1.2)
        m.initial('NADH', 3)
        
        self.add_states('metabolites', m)
        self.add_simulation('FBA', fba.ReactionFBA(self, m))

if __name__ == '__main__':
    #external_environment = ExtracellularEnvironment()
    s = core.Simulator()
    
    s.add_structure('cell1',EcoliCell())
  
    
    #external_transport = MembraneTransport(external_environment, cell)
    #s.add(external_transport)
        
    s.build()
    
    print s.state.simulations
    print s.state.structures
    print s.state.groups
    
    s.step()
    s.step()
    
    