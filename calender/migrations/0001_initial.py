# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Events'
        db.create_table(u'calender_events', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campus', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('end', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'calender', ['Events'])


    def backwards(self, orm):
        # Deleting model 'Events'
        db.delete_table(u'calender_events')


    models = {
        u'calender.events': {
            'Meta': {'object_name': 'Events'},
            'campus': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['calender']