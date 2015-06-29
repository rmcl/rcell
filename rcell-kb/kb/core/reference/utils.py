import reference.models as reference_models

def formatted_citation(reference, as_html = False):
    '''
    Format a reference for display as HTML
    '''
    ref = reference.as_subclass()
    if isinstance(ref, reference_models.LiteratureReference):
        if ref.literature_type == 'ARTICLE':
            if as_html is True:
                return '%s. %s. <i>%s</i> <b>%s</b>, %s (%s).' % (ref.authors, ref.title,
                    ref.publication, ref.volume, ref.pages, ref.year, )
            else:
                return '%s. %s. %s %s, %s (%s).' % (ref.authors, ref.title,
                    ref.publication, ref.volume, ref.pages, ref.year, )
        
        return '%s: %s' % (ref.literature_type, ref.title)

    return str(ref)
    
reference_models.Reference.__unicode__ = lambda self: formatted_citation(self)