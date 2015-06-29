from django.contrib import admin

import reaction.models as reaction_models
import molecule.utils as molecule_utils

class ReactionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('display_reaction',)
    
    fieldsets = (
        (None, {
            'fields': ('name', )
        }), ('Details', {
            'fields': ('display_reaction',)
        }), ('References', {
            'fields': ('comments', 'references')
        })
        
    )
   
    def display_reaction(self, reaction):
        out = ''
        short = ''
        for idx, participant in enumerate(reaction.participants):
            c = participant.coefficient
            if c == 1.0 and idx > 0:
                c = '+'
            elif c == 1.0:
                c = ''
            elif c == -1.0:
                c = '-'
                
            c = str(c)
            
            empirical_formula = molecule_utils.parse_empirical_formula(participant.molecule.empirical_formula,
                as_html=True)
            
            short += '%s%s' % (c, participant.molecule)
            out += '%s%s' % (c, empirical_formula)
        
            bla = 'Short: %s<br/>Full: %s' % (short, out)
        
        return bla

    display_reaction.short_description = 'Equation'
    display_reaction.allow_tags = True

admin.site.register(reaction_models.Reaction, ReactionAdmin)

class ReactionParticipantAdmin(admin.ModelAdmin):
    list_display = ('reaction', 'molecule', 'coefficient')

admin.site.register(reaction_models.ReactionParticipant, ReactionParticipantAdmin)