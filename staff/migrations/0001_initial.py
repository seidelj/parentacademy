# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Staff'
        db.create_table(u'staff_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('picture_url', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'staff', ['Staff'])


    def backwards(self, orm):
        # Deleting model 'Staff'
        db.delete_table(u'staff_staff')


    models = {
        u'staff.staff': {
            'Meta': {'object_name': 'Staff'},
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['staff']