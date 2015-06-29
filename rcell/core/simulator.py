import states as core_state
import structure as core_structure
'''
class Breakpoint(object):
    ''
    A class to stop a running simulation if some conditions are met. Can be
    based on the state of some variable or the time step itself. 
    ''
    def __init__(self, time_step):
        pass
        
    def 

'''
    
class Simulator(core_structure.StructureContainerMixin):

    def add_simulation(self, simulation):
        '''
        Add a simulation to the execution list.
        '''
        try:
            if simulation in self._simulations:
                self._simulations_ordered.append(simulation)
                self._simulations.add(simulation)
        except AttributeError:
            self._simulations_ordered = [ simulation ]
            self._simulations = { simulation }
    
    def build(self):
        '''
        Construct initial state and initialize the structures.
        '''
        self.state = core_state.SimulatorState()
        
        # Add all of the state groups for all of the structures in all of the
        # simulations to the global state vector.
        try:
            for simulation in self._simulations:
                self.state = simulation.build(self.state)
        except AttributeError:
            # No sub simulations
            pass

        try:
            for name, structure in self.structures.items():
                self.state = structure.build(self.state)
        except AttributeError:
            # No sub structures
            pass
            
        # Generate the state vector
        self.state.build_state_vector()
        
        
        
    
    def step(self):
        for simulation in self.state.simulations:
            check = self.state.clock / simulation.time_step
            if abs(round(check) - check) >1e-9:
                continue
            
            # Extract relevant states for this simulation
            states = {}
            for struct_name, struct in simulation.structures.items():
                struct_states = {}
                for group_name, group in struct.states.items():
                    struct_states[group_name] = group.extract_state(self.state.states)

                states[struct_name] = struct_states
            
            # Run the simulation
            updated_state = simulation.update(self.state.clock, states)
            
            # Update the states with the modified states
            for struct_name, struct in simulation.structures.items():
                for group_name, group in struct.states.items():
                    group.update_state(self.state.states, updated_state[struct_name][group_name])
            
        self.state.clock += self.state.time_step
        
    def run(self):
        '''
        Start the simulation and let it run.
        '''
        pass