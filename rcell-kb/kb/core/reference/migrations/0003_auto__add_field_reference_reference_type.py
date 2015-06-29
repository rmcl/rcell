# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reference.reference_type'
        db.add_column('reference_reference', 'reference_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Reference.reference_type'
        db.delete_column('reference_reference', 'reference_type_id')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'reference.internetreference': {
            'Meta': {'object_name': 'InternetReference', '_ormbases': ['reference.Reference']},
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'reference_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['reference.Reference']", 'unique': 'True', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'reference.literaturereference': {
            'Meta': {'object_name': 'LiteratureReference', '_ormbases': ['reference.Reference']},
            'authors': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'editors': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'issue': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'literature_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'pages': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'publication': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'reference_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['reference.Reference']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'volume': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'reference.reference': {
            'Meta': {'object_name': 'Reference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'})
        }
    }

    complete_apps = ['reference']