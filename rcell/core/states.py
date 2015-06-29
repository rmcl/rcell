import numpy as np

class SimulatorState(object):
    def __init__(self):
        # A numpy vector defining the actual states of the simulation.
        self.states = None

        # The length of the state vector
        self.state_len = 0
        
        # A set of all state groups defined in the various structures of the
        # simulation.
        self.groups = set()
        
        self.simulations = set()
        
        # A set of structures in all of the simulations
        self.structures = set()

        # The current simulation step of the simulation.
        self.clock = 0
        
        # The smallest time step required to satisfy all simulations
        self.time_step = 1.0

    def add_simulation(self, simulation):
        self.simulations.add(simulation)

    def add_structure(self, structure):
        '''
        Add a structure to the simulator
        '''
        if self.states is not None:
            raise core_exceptions.StateVectorAlreadyGenerated('Cannot add \
                structures after state vector has been generated.')
                
        if structure not in self.structures:
            self.structures.add(structure)
            
            # Add all of the structures groups to the state vector
            for group_name, state_group in structure.states.iteritems():
                self.add_group(state_group)

    def structure_already_added(self, structure):
        return structure in self.structures

    def add_group(self, state_group):
        '''
        Add a state group to the simulator.
        '''
        if self.states is not None:
            raise core_exceptions.StateVectorAlreadyGenerated('Cannot add state \
                groups after state vector has been generated.')
        
        if state_group not in self.groups:
            self.groups.add(state_group)
            state_group.start_pos = self.state_len
            self.state_len += state_group.size

    def build_state_vector(self):
        '''
        Build global state vector. Length of vector is specified by the
        state_len property. Once this is generated cannot add new structures
        or state groups.
        '''
        if self.states is not None:
            raise core_exceptions.StateVectorAlreadyGenerated('The state vector \
                has already been generated.')
            
        self.states = np.zeros((self.state_len,))

class StateGroup(object):
    '''
    Define a continuous subset of the global architecture state vector. Also 
    provide some logical mapping to more useful keys.
    '''
    def __init__(self, size):
        self.size = size
        self.start_pos = None
    
    def extract_state(self, state_vector):
        '''
        Extract the relevant portion of the state vector from
        the global state vector
        '''
        end_pos = self.start_pos+self.size
        return state_vector[self.start_pos:end_pos]
        
    def update_state(self, state_vector, updated_state):
        '''
        update the global state with the updated state slice.
        '''
        end_pos = self.start_pos+self.size
        state_vector[self.start_pos:end_pos] = updated_state
                
    def init_states(self):
        '''
        Before the simulation starts you have to opportunity to initialize the state vector.
        '''
        pass