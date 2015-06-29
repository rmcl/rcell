# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Molecule'
        db.create_table('molecule_molecule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('traditional_name', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('iupac_name', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('empirical_formula', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('molecule', ['Molecule'])


    def backwards(self, orm):
        # Deleting model 'Molecule'
        db.delete_table('molecule_molecule')


    models = {
        'molecule.molecule': {
            'Meta': {'object_name': 'Molecule'},
            'empirical_formula': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iupac_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'traditional_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['molecule']