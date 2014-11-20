# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Events.date'
        db.delete_column(u'calender_events', 'date')

        # Adding field 'Events.eventdate'
        db.add_column(u'calender_events', 'eventdate',
                      self.gf('django.db.models.fields.DateField')(default='2014-01-01'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Events.date'
        db.add_column(u'calender_events', 'date',
                      self.gf('django.db.models.fields.DateField')(default='2014-01-01'),
                      keep_default=False)

        # Deleting field 'Events.eventdate'
        db.delete_column(u'calender_events', 'eventdate')


    models = {
        u'calender.events': {
            'Meta': {'object_name': 'Events'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'council': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            'eventdate': ('django.db.models.fields.DateField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['calender']