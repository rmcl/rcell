import unittest
import numpy as np

import rcell.kb.reactions as reactions


class Test(unittest.TestCase):

    def test_build_stoichiometry_matrix(self):
        result = reactions.build_stoichiometry_matrix(
            self.inp_reactions_ex2)

        self.assertEquals((5, 4), result['N'].shape)
        self.assertEquals(4, len(result['reactions']))
        self.assertEquals(5, len(result['participants']))

    inp_reaction_ex2_res = np.array([
        [-1., 0., 0., 1.],
        [1., 0., 0., 0.],
        [0., -1., 0., 0.],
        [0., 1., 1., 0.],
        [0., 0., -1., -1.]
    ])

    inp_reactions_ex2 = {
        'R1': [[-1.0, 'S1'], [1.0, 'S2']],
        'R2': [[-5.0, 'S3'], [-1.0, 'S2'], [4, 'S3'], [2, 'S2']],
        'R3': [[-1, 'S3'], [1, 'S4']],
        'R4': [[-1, 'S4'], [1, 'S5']]
    }

    inp_reactions_ex1 = {
        'R1': [[-1.0, 'A'], [-1.0, 'ATP'], [1.0, 'B']],
        'R2a': [[-1.0, 'B'], [2.0, 'ATP'], [2.0, 'NADH'], [1.0, 'C']],
        'R2b': [[-1.0, 'C'], [-2.0, 'ATP'], [-2.0, 'NADH'], [1.0, 'B']],
        'R5a': [[-1.0, 'G'], [0.8, 'C'], [2.0, 'NADH']],
        'R5b': [[-1.0, 'G'], [0.8, 'C'], [2.0, 'NADH']],
        'R6': [[-1.0, 'C'], [2.0, 'ATP'], [3.0, 'D']],
        'R7': [[-1.0, 'C'], [-4.0, 'NADH'], [3.0, 'E']],
        'R8a': [[-1.0, 'G'], [1.0, 'ATP'], [-2.0, 'NADH'], [1.0, 'H']],
        'R8b': [[1.0, 'G'], [1.0, 'ATP'], [2.0, 'NADH'], [-1.0, 'H']],
        'Rres': [[-1.0, 'NADH'], [-1.0, 'O2'], [1.0, 'ATP']]
    }


if __name__ == '__main__':
    unittest.main()
