# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Actor'
        db.create_table(u'actors_actor', (
            (u'basemodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['common.BaseModel'], unique=True, primary_key=True)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('height', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('is_alive', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('birthday', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('birthmonth', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('birthyear', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'actors', ['Actor'])

        # Adding model 'Role'
        db.create_table(u'actors_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['actors.Actor'])),
            ('media_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('media_type', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('character', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'actors', ['Role'])


    def backwards(self, orm):
        # Deleting model 'Actor'
        db.delete_table(u'actors_actor')

        # Deleting model 'Role'
        db.delete_table(u'actors_role')


    models = {
        u'actors.actor': {
            'Meta': {'object_name': 'Actor', '_ormbases': [u'common.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['common.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'birthday': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birthmonth': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_alive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'actors.role': {
            'Meta': {'object_name': 'Role'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['actors.Actor']"}),
            'character': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'media_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'common.basemodel': {
            'Meta': {'object_name': 'BaseModel'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fan.FanUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'fan.fanuser': {
            'Meta': {'object_name': 'FanUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_contributor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['actors']