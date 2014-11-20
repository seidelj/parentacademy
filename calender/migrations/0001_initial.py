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
            ('council', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'calender', ['Events'])


    def backwards(self, orm):
        # Deleting model 'Events'
        db.delete_table(u'calender_events')


    models = {
        u'calender.events': {
            'Meta': {'object_name': 'Events'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'council': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['calender']