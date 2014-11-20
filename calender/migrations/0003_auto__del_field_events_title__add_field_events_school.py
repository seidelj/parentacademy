# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Events.title'
        db.delete_column(u'calender_events', 'title')

        # Adding field 'Events.school'
        db.add_column(u'calender_events', 'school',
                      self.gf('django.db.models.fields.CharField')(default='blah', max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Events.title'
        db.add_column(u'calender_events', 'title',
                      self.gf('django.db.models.fields.CharField')(default='blah', max_length=256),
                      keep_default=False)

        # Deleting field 'Events.school'
        db.delete_column(u'calender_events', 'school')


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
            'school': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'start': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['calender']