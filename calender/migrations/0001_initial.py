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
            ('eventdate', self.gf('django.db.models.fields.DateField')()),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'calender', ['Events'])

        # Adding model 'CalenderPlugin'
        db.create_table(u'calender_calenderplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('events', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calender.Events'])),
        ))
        db.send_create_signal(u'calender', ['CalenderPlugin'])


    def backwards(self, orm):
        # Deleting model 'Events'
        db.delete_table(u'calender_events')

        # Deleting model 'CalenderPlugin'
        db.delete_table(u'calender_calenderplugin')


    models = {
        u'calender.calenderplugin': {
            'Meta': {'object_name': 'CalenderPlugin', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'events': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['calender.Events']"})
        },
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
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['calender']