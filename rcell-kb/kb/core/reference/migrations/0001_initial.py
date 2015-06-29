# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reference'
        db.create_table('reference_reference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('reference', ['Reference'])

        # Adding model 'LiteratureReference'
        db.create_table('reference_literaturereference', (
            ('reference_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reference.Reference'], unique=True, primary_key=True)),
            ('authors', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('editors', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('publication', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('volume', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('issue', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('pages', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal('reference', ['LiteratureReference'])

        # Adding model 'InternetReference'
        db.create_table('reference_internetreference', (
            ('reference_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reference.Reference'], unique=True, primary_key=True)),
            ('external_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('reference', ['InternetReference'])


    def backwards(self, orm):
        # Deleting model 'Reference'
        db.delete_table('reference_reference')

        # Deleting model 'LiteratureReference'
        db.delete_table('reference_literaturereference')

        # Deleting model 'InternetReference'
        db.delete_table('reference_internetreference')


    models = {
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['reference']