# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Experience.description_2'
        db.add_column('resume_app_experience', 'description_2',
                      self.gf('django.db.models.fields.CharField')(default=True, max_length=250),
                      keep_default=False)

        # Adding field 'Experience.description_3'
        db.add_column('resume_app_experience', 'description_3',
                      self.gf('django.db.models.fields.CharField')(default=True, max_length=250),
                      keep_default=False)


        # Changing field 'Experience.end_date'
        db.alter_column('resume_app_experience', 'end_date', self.gf('django.db.models.fields.DateField')(auto_now=True))

    def backwards(self, orm):
        # Deleting field 'Experience.description_2'
        db.delete_column('resume_app_experience', 'description_2')

        # Deleting field 'Experience.description_3'
        db.delete_column('resume_app_experience', 'description_3')


        # Changing field 'Experience.end_date'
        db.alter_column('resume_app_experience', 'end_date', self.gf('django.db.models.fields.DateField')())

    models = {
        'resume_app.experience': {
            'Meta': {'object_name': 'Experience'},
            'begin_date': ('django.db.models.fields.DateField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description_2': ('django.db.models.fields.CharField', [], {'default': 'True', 'max_length': '250'}),
            'description_3': ('django.db.models.fields.CharField', [], {'default': 'True', 'max_length': '250'}),
            'end_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'resume_app.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip': ('django.db.models.fields.IntegerField', [], {'default': 'True', 'max_length': '5'})
        },
        'resume_app.projects': {
            'Meta': {'object_name': 'Projects'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'resume_app.skills': {
            'Meta': {'object_name': 'Skills'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['resume_app']