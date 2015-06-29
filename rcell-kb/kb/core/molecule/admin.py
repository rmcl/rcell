from django.contrib import admin

import molecule.utils as molecule_utils
import molecule.models as molecule_models

class MoleculeAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'name', 'empirical_formula_formatted', 'iupac_name')

    def empirical_formula_formatted(self, obj):
        return molecule_utils.parse_empirical_formula(obj.empirical_formula,
            as_html=True)
        
    empirical_formula_formatted.admin_order_field = 'empirical_formula'
    empirical_formula_formatted.short_description = 'Empirical Formula'
    empirical_formula_formatted.allow_tags = True

admin.site.register(molecule_models.Molecule, MoleculeAdmin)