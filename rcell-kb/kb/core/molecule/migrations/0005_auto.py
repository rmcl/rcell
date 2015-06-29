# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field references on 'Molecule'
        db.create_table('molecule_molecule_references', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('molecule', models.ForeignKey(orm['molecule.molecule'], null=False)),
            ('reference', models.ForeignKey(orm['reference.reference'], null=False))
        ))
        db.create_unique('molecule_molecule_references', ['molecule_id', 'reference_id'])


    def backwards(self, orm):
        # Removing M2M table for field references on 'Molecule'
        db.delete_table('molecule_molecule_references')


    models = {
        'molecule.molecule': {
            'Meta': {'object_name': 'Molecule'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'empirical_formula': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iupac_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reference.Reference']", 'symmetrical': 'False'}),
            'traditional_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        'reference.reference': {
            'Meta': {'object_name': 'Reference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['molecule']