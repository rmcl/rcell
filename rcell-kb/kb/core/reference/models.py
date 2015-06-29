from django.db import models
import django.contrib.contenttypes.models as contenttype_models



class ReferenceMixin(models.Model):
    '''
    A abstract model which give a inheriting model the ability to link
    references.
    '''
    comments = models.TextField(blank=True)
    references = models.ManyToManyField('Reference', blank=True)

    class Meta:
        abstract = True

class Reference(models.Model):
    # A reference to the subtype of this reference entry so we can identify
    # the subtype without an extra query.
    reference_type = models.ForeignKey(contenttype_models.ContentType,
        editable=False, null=True)

    def as_subclass(self):
        if self.reference_type is None:
            return self
            
        model = self.reference_type.model_class()
        if (model == Reference):
            return self
        return model.objects.get(id=self.id)

    def save(self, *args, **kwargs):
        '''
        Override the save method to store the content type of the child model
        '''
        if not self.reference_type:
            self.reference_type = contenttype_models.ContentType.objects.get_for_model(self.__class__)
            
        super(Reference, self).save(*args, **kwargs)    

LITERATURE_TYPES = (
    ('BOOK', 'Book'),
    ('ARTICLE', 'Article'),
    ('THESIS', 'Thesis'),        
)

class LiteratureReference(Reference):
    '''
    Reference to an article, book, etc in the literature.
    '''
    literature_type = models.CharField(max_length=10, choices=LITERATURE_TYPES)
    
    authors = models.TextField(blank=True, default='', verbose_name='Author(s)')
    editors = models.TextField(blank=True, default='', verbose_name='Editor(s)')
    year = models.IntegerField(blank=True, null=True, verbose_name='Year')
    title = models.TextField(blank=True, default='', verbose_name='Title')
    publication = models.CharField(max_length=255, blank=True, default='', verbose_name='Publication')
    publisher = models.CharField(max_length=255, blank=True, default='', verbose_name='Publisher')
    volume = models.CharField(max_length=255, blank=True, default='', verbose_name='Volume')
    issue = models.CharField(max_length=255, blank=True, default='', verbose_name='Issue')
    pages = models.CharField(max_length=255, blank=True, default='', verbose_name='Page(s)')
    
    

INTERNET_REFERENCE_SOURCES = (
    ('ATCC', 'ATCC'),
    ('BiGG', 'BiGG'),
    ('BioCyc', 'BioCyc'),
    ('BioProject', 'BioProject'), #http://www.ncbi.nlm.nih.gov/bioproject/%s
    ('CAS', 'CAS'),
    ('ChEBI', 'ChEBI'),
    ('CMR', 'CMR'),
    ('EC', 'EC'),
    ('GenBank', 'GenBank'),
    ('ISBN', 'ISBN'),
    ('KEGG', 'KEGG'),
    ('KNApSAcK', 'KNApSAcK'),
    ('LipidBank', 'LipidBank'),
    ('LIPIDMAPS', 'LIPIDMAPS'),
    ('PDB', 'PDB'),
    ('PDBCCD', 'PDBCCD'),
    ('PubChem', 'PubChem'),
    ('PubMed', 'PubMed'),
    ('RefSeq', 'RefSeq'),
    ('SABIO-RK', 'SABIO-RK'),
    ('SwissProt', 'SwissProt'),
    ('Taxonomy', 'Taxonomy'),
    ('ThreeDMET', 'ThreeDMET'), 
    ('URL', 'URL'),
)   
        
class InternetReference(Reference):
    '''
    A reference to one of the many only databases or websites
    '''
    external_id = models.CharField(max_length=255, verbose_name='External ID')
    source = models.CharField(max_length=20, choices=INTERNET_REFERENCE_SOURCES, verbose_name='Source')

    class Meta:
        verbose_name='Internet reference'
        verbose_name_plural = 'Internet references'
        
    def __unicode__(self):
        return '%s: %s' % (self.source, self.external_id)