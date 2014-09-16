# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Staff.about'
        db.add_column(u'staff_staff', 'about',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Staff.about'
        db.delete_column(u'staff_staff', 'about')


    models = {
        u'staff.staff': {
            'Meta': {'object_name': 'Staff'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'picture_url': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['staff']