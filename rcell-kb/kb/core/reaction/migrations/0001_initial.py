# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reaction'
        db.create_table('reaction_reaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
        ))
        db.send_create_signal('reaction', ['Reaction'])

        # Adding model 'ReactionParticipant'
        db.create_table('reaction_reactionparticipant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reaction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reaction.Reaction'])),
            ('coefficient', self.gf('django.db.models.fields.FloatField')()),
            ('molecule', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['molecule.Molecule'])),
        ))
        db.send_create_signal('reaction', ['ReactionParticipant'])


    def backwards(self, orm):
        # Deleting model 'Reaction'
        db.delete_table('reaction_reaction')

        # Deleting model 'ReactionParticipant'
        db.delete_table('reaction_reactionparticipant')


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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        'reaction.reactionparticipant': {
            'Meta': {'object_name': 'ReactionParticipant'},
            'coefficient': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'molecule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['molecule.Molecule']"}),
            'reaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reaction.Reaction']"})
        }
    }

    complete_apps = ['reaction']