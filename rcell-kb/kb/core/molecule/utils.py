import re

def parse_empirical_formula(formula, as_html=False):
    '''
    Given an empirical formula as a string, parse it and optionally format it.
    
    :param formala: The empirical formula in string form.
    :type formula: str
    :param as_html: Optional parameter. if true, Return parsed formula as html
    :returns: List of tuples containing the component pieces of the formula OR
        if as_html is True returns string of html.
    '''
    parsed = list((match.group(1), match.group(2)) for 
                  match in re.finditer(r'([A-Z][a-z]*)([0-9]*)', formula))

    if as_html is True:
        return ''.join(map(lambda x:'%s<sub>%s</sub>' % (x), parsed))

    return parsed
