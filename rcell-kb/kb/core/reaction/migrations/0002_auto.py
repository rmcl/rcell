# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field references on 'Reaction'
        db.create_table('reaction_reaction_references', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reaction', models.ForeignKey(orm['reaction.reaction'], null=False)),
            ('reference', models.ForeignKey(orm['reference.reference'], null=False))
        ))
        db.create_unique('reaction_reaction_references', ['reaction_id', 'reference_id'])

        # Adding M2M table for field references on 'ReactionParticipant'
        db.create_table('reaction_reactionparticipant_references', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reactionparticipant', models.ForeignKey(orm['reaction.reactionparticipant'], null=False)),
            ('reference', models.ForeignKey(orm['reference.reference'], null=False))
        ))
        db.create_unique('reaction_reactionparticipant_references', ['reactionparticipant_id', 'reference_id'])


    def backwards(self, orm):
        # Removing M2M table for field references on 'Reaction'
        db.delete_table('reaction_reaction_references')

        # Removing M2M table for field references on 'ReactionParticipant'
        db.delete_table('reaction_reactionparticipant_references')


    models = {
        'molecule.molecule': {
            'Meta': {'object_name': 'Molecule'},
            'empirical_formula': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iupac_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'traditional_name': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'})
        },
        'reaction.reaction': {
            'Meta': {'object_name': 'Reaction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reference.Reference']", 'symmetrical': 'False'})
        },
        'reaction.reactionparticipant': {
            'Meta': {'object_name': 'ReactionParticipant'},
            'coefficient': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'molecule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['molecule.Molecule']"}),
            'reaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reaction.Reaction']"}),
            'references': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['reference.Reference']", 'symmetrical': 'False'})
        },
        'reference.reference': {
            'Meta': {'object_name': 'Reference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['reaction']