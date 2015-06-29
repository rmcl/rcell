from django.contrib import admin

import reference.utils as reference_utils
import reference.models as reference_models


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'formatted_citation',)
    
    def formatted_citation(self, obj):
        return reference_utils.formatted_citation(obj)
            
    formatted_citation.short_description = 'Citation'
    formatted_citation.allow_tags = True
    
admin.site.register(reference_models.Reference, ReferenceAdmin)

#admin.site.register(reference_models.Reference)
admin.site.register(reference_models.InternetReference)
admin.site.register(reference_models.LiteratureReference)