import rcell.core as core

class MembraneTransport(core.Simulation):
    def __init__(self, c1, c2):
        self.add_structure('c1', c1)
        self.add_structure('c2', c2)