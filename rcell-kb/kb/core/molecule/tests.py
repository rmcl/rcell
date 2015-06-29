"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

import molecule.utils as molecule_utils

class ParseEmpiricalFormulaTest(TestCase):
    def test_formula_2_html_test(self):
        """
        Confirm that we can parse an empirical formula into html
        """
        formula = 'H12C10N5O13P3'
        
        parsed = molecule_utils.parse_empirical_formula(formula, as_html = True)
        expected_out = 'H<sub>12</sub>C<sub>10</sub>N<sub>5</sub>O<sub>13</sub>P<sub>3</sub>'
        self.assertEqual(parsed, expected_out, 'HTML output does not match expected value')

    def test_formula_parsed(self):
        formula = 'H12C10N5O13P3'
        
        parsed = molecule_utils.parse_empirical_formula(formula)
        expected_out = [('H', '12'), ('C', '10'), ('N', '5'), ('O', '13'), ('P', '3')]
        
        self.assertEqual(parsed, expected_out, 'output does not match expected value')
        