import structure

class Simulation(structure.StructureContainerMixin):
    
    def __init__(self):
        pass
    
    def set_time_step(self, time_step):
        self.time_step = time_step
        


    def build(self, state):
        state.add_simulation(self)
        for structure_name, structure in self.structures.iteritems():
            state = structure.build(state)
            
        return state