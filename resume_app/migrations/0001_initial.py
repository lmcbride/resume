# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('resume_app_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('zip', self.gf('django.db.models.fields.IntegerField')(default=True, max_length=5)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('resume_app', ['Person'])

        # Adding model 'Skills'
        db.create_table('resume_app_skills', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['resume_app.Category'], null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
        ))
        db.send_create_signal('resume_app', ['Skills'])

        # Adding model 'Category'
        db.create_table('resume_app_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
        ))
        db.send_create_signal('resume_app', ['Category'])

        # Adding model 'Projects'
        db.create_table('resume_app_projects', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('resume_app', ['Projects'])

        # Adding model 'Experience'
        db.create_table('resume_app_experience', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('begin_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description_2', self.gf('django.db.models.fields.CharField')(default=True, max_length=250)),
            ('description_3', self.gf('django.db.models.fields.CharField')(default=True, max_length=250)),
        ))
        db.send_create_signal('resume_app', ['Experience'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('resume_app_person')

        # Deleting model 'Skills'
        db.delete_table('resume_app_skills')

        # Deleting model 'Category'
        db.delete_table('resume_app_category')

        # Deleting model 'Projects'
        db.delete_table('resume_app_projects')

        # Deleting model 'Experience'
        db.delete_table('resume_app_experience')


    models = {
        'resume_app.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        },
        'resume_app.experience': {
            'Meta': {'object_name': 'Experience'},
            'begin_date': ('django.db.models.fields.DateField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'description_2': ('django.db.models.fields.CharField', [], {'default': 'True', 'max_length': '250'}),
            'description_3': ('django.db.models.fields.CharField', [], {'default': 'True', 'max_length': '250'}),
            'end_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['resume_app.Category']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['resume_app']