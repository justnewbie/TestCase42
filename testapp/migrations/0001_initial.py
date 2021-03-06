# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'testapp_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('b_date', self.gf('django.db.models.fields.DateField')()),
            ('about', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=50, blank=True)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'testapp', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'testapp_person')


    models = {
        u'testapp.person': {
            'Meta': {'object_name': 'Person'},
            'about': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'b_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['testapp']