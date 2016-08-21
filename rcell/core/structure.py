import exceptions


class StructureContainerMixin(object):
    def add_structure(self, name, structure):
        try:
            if name in self._structures:
                raise exceptions.StructureNameConflict('A structure with that name already exists.')

            self._structures[name] = structure
        except AttributeError:
            self._structures = {
                name: structure
            }

    def _get_structures(self):
        "Return a set of all structure."

        try:
            return self._structures
        except AttributeError:
            return {}
    structures = property(_get_structures)


class Structure(StructureContainerMixin):
    '''
    A abstract compartment. Not neccessarily spatially distinct, but distinct somehow.
    '''
    def __init__(self):
        # Define how frequently this structure should be executed
        self.time_step = 1

    def add_states(self, name, state_group):
        '''
        Attach a state group to this structure.
        '''
        try:
            self._state_groups[name] = state_group
        except AttributeError:
            self._state_groups = { name: state_group }

    def _get_states(self):
        '''
        Get the state groups that this structure has defined.
        :returns: dict containg the state groups
        '''
        try:
            return self._state_groups
        except AttributeError:
            return {}
    states = property(_get_states)

    def add_simulation(self, name, simulation):
        try:
            self._simulations[name] = simulation
        except AttributeError:
            self._simulations = { name: simulation }

    def build(self, state):
        if not state.structure_already_added(self):
            state.add_structure(self)

            for name, sim in self._simulations.items():
                state = sim.build(state)

        return state


class Compartment(Structure):
    '''
    A spatial region enclosed by some sort of membrane.
    '''
    pass
