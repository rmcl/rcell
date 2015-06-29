# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Molecule.name'
        db.delete_column('molecule_molecule', 'name')

        # Adding field 'Molecule.acronym'
        db.add_column('molecule_molecule', 'acronym',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Molecule.name'
        raise RuntimeError("Cannot reverse this migration. 'Molecule.name' and its values cannot be restored.")
        # Deleting field 'Molecule.acronym'
        db.delete_column('molecule_molecule', 'acronym')


    models = {
        'molecule.molecule': {
            'Meta': {'object_name': 'Molecule'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'empirical_formula': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iupac_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'traditional_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        }
    }

    complete_apps = ['molecule']