import logging
import reaction.models as reaction_models

logger = logging.getLogger(__name__)


def dot_reaction_graph():

    reactions = reaction_models.Reaction.objects.all()
    
    nodes = set()
    links = set()

    print 'digraph G {'
    
    for reaction in reactions:
        
        nodes.add(('reaction', reaction.name))
        
        source, sink = [], []
        for particip in reaction.participants:
            if particip.coefficient < 0:
                # Source 
                links.add((particip.molecule, reaction.name))
            else:
                links.add((reaction.name, particip.molecule))
            
        
    for s,t in links:
            try:
                src = s.molecule.acronym
            except:
                src = s

            try:
                trg = t.molecule.acronym
            except:
                trg = t
                
            print '%s -> %s;' % (src, trg)
    
    for ntype, name  in nodes:
        if ntype == 'reaction':
            print '%s [shape=polygon,sides=5,peripheries=3,color=lightblue,style=filled]' % (name)
        else:
            pass
        
    print '}'


def mol_network():
    reactions = reaction_models.Reaction.objects.all()
    
    links = set()
    for reaction in reactions:
        source, sink = [], []
        for particip in reaction.participants:
            if particip.coefficient < 0:
                source.append(particip)
            else:
                sink.append(particip)
            
        
        for s in source:
            for t in sink:
                links.add((s.molecule, t.molecule))
    
    print 'digraph G {'
    for s,t in links:
        print '%s -> %s;' % (s.acronym, t.acronym)
    print '}'