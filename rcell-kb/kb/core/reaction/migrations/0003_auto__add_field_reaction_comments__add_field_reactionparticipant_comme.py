# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reaction.comments'
        db.add_column('reaction_reaction', 'comments',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'ReactionParticipant.comments'
        db.add_column('reaction_reactionparticipant', 'comments',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Reaction.comments'
        db.delete_column('reaction_reaction', 'comments')

        # Deleting field 'ReactionParticipant.comments'
        db.delete_column('reaction_reactionparticipant', 'comments')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'molecule.molecule': {
            'Meta': {'object_name': 'Molecule'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'empirical_formula': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iupac_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reference.Reference']", 'symmetrical': 'False', 'blank': 'True'}),
            'traditional_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        'reaction.reaction': {
            'Meta': {'object_name': 'Reaction'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reference.Reference']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'reaction.reactionparticipant': {
            'Meta': {'object_name': 'ReactionParticipant'},
            'coefficient': ('django.db.models.fields.FloatField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'molecule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['molecule.Molecule']"}),
            'reaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reaction.Reaction']"}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reference.Reference']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'reference.reference': {
            'Meta': {'object_name': 'Reference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'})
        }
    }

    complete_apps = ['reaction']