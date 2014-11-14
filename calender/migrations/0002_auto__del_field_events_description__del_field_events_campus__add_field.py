# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Events.description'
        db.delete_column(u'calender_events', 'description')

        # Deleting field 'Events.campus'
        db.delete_column(u'calender_events', 'campus')

        # Adding field 'Events.council'
        db.add_column(u'calender_events', 'council',
                      self.gf('django.db.models.fields.CharField')(default='2', max_length=3),
                      keep_default=False)

        # Adding field 'Events.location'
        db.add_column(u'calender_events', 'location',
                      self.gf('django.db.models.fields.TextField')(default='2'),
                      keep_default=False)

        # Adding field 'Events.group'
        db.add_column(u'calender_events', 'group',
                      self.gf('django.db.models.fields.CharField')(default='2', max_length=128),
                      keep_default=False)

        # Adding field 'Events.color'
        db.add_column(u'calender_events', 'color',
                      self.gf('django.db.models.fields.CharField')(default='2', max_length=128),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Events.description'
        db.add_column(u'calender_events', 'description',
                      self.gf('django.db.models.fields.TextField')(default='2'),
                      keep_default=False)

        # Adding field 'Events.campus'
        db.add_column(u'calender_events', 'campus',
                      self.gf('django.db.models.fields.CharField')(default='2', max_length=3),
                      keep_default=False)

        # Deleting field 'Events.council'
        db.delete_column(u'calender_events', 'council')

        # Deleting field 'Events.location'
        db.delete_column(u'calender_events', 'location')

        # Deleting field 'Events.group'
        db.delete_column(u'calender_events', 'group')

        # Deleting field 'Events.color'
        db.delete_column(u'calender_events', 'color')


    models = {
        u'calender.events': {
            'Meta': {'object_name': 'Events'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'council': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'end': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'start': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['calender']