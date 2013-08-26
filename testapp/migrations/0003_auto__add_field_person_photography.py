# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.photography'
        db.add_column(u'testapp_person', 'photography',
                      self.gf('django.db.models.fields.files.ImageField')(default='images/test.jpg', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.photography'
        db.delete_column(u'testapp_person', 'photography')


    models = {
        u'testapp.person': {
            'Meta': {'object_name': 'Person'},
            'about': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'b_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'photography': ('django.db.models.fields.files.ImageField', [], {'default': "'images/test.jpg'", 'max_length': '100'})
        },
        u'testapp.requestlogs': {
            'Meta': {'object_name': 'RequestLogs'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'time_stamp': ('django.db.models.fields.DateField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['testapp']