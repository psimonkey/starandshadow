# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Film.startDate'
        db.add_column('programming_film', 'startDate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'Film.startTime'
        db.add_column('programming_film', 'startTime',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 19, 10, 277000)),
                      keep_default=False)

        # Adding field 'Festival.startDate'
        db.add_column('programming_festival', 'startDate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'Festival.startTime'
        db.add_column('programming_festival', 'startTime',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 19, 10, 280000)),
                      keep_default=False)

        # Adding field 'Festival.endDate'
        db.add_column('programming_festival', 'endDate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'Festival.endTime'
        db.add_column('programming_festival', 'endTime',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 19, 10, 280000)),
                      keep_default=False)

        # Adding field 'Gig.startDate'
        db.add_column('programming_gig', 'startDate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'Gig.startTime'
        db.add_column('programming_gig', 'startTime',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 19, 10, 278000)),
                      keep_default=False)

        # Adding field 'Gig.endTime'
        db.add_column('programming_gig', 'endTime',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 19, 10, 278000)),
                      keep_default=False)

        # Adding field 'Season.startDate'
        db.add_column('programming_season', 'startDate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'Season.endDate'
        db.add_column('programming_season', 'endDate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.startDate'
        db.add_column('programming_event', 'startDate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.startTime'
        db.add_column('programming_event', 'startTime',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 19, 10, 279000)),
                      keep_default=False)

        # Adding field 'Event.endTime'
        db.add_column('programming_event', 'endTime',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 19, 10, 279000)),
                      keep_default=False)

        # Adding field 'Meeting.startDate'
        db.add_column('programming_meeting', 'startDate',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 12, 13, 0, 0)),
                      keep_default=False)

        # Adding field 'Meeting.startTime'
        db.add_column('programming_meeting', 'startTime',
                      self.gf('django.db.models.fields.TimeField')(default=datetime.time(0, 19, 10, 282000)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Film.startDate'
        db.delete_column('programming_film', 'startDate')

        # Deleting field 'Film.startTime'
        db.delete_column('programming_film', 'startTime')

        # Deleting field 'Festival.startDate'
        db.delete_column('programming_festival', 'startDate')

        # Deleting field 'Festival.startTime'
        db.delete_column('programming_festival', 'startTime')

        # Deleting field 'Festival.endDate'
        db.delete_column('programming_festival', 'endDate')

        # Deleting field 'Festival.endTime'
        db.delete_column('programming_festival', 'endTime')

        # Deleting field 'Gig.startDate'
        db.delete_column('programming_gig', 'startDate')

        # Deleting field 'Gig.startTime'
        db.delete_column('programming_gig', 'startTime')

        # Deleting field 'Gig.endTime'
        db.delete_column('programming_gig', 'endTime')

        # Deleting field 'Season.startDate'
        db.delete_column('programming_season', 'startDate')

        # Deleting field 'Season.endDate'
        db.delete_column('programming_season', 'endDate')

        # Deleting field 'Event.startDate'
        db.delete_column('programming_event', 'startDate')

        # Deleting field 'Event.startTime'
        db.delete_column('programming_event', 'startTime')

        # Deleting field 'Event.endTime'
        db.delete_column('programming_event', 'endTime')

        # Deleting field 'Meeting.startDate'
        db.delete_column('programming_meeting', 'startDate')

        # Deleting field 'Meeting.startTime'
        db.delete_column('programming_meeting', 'startTime')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'fileupload.picture': {
            'Meta': {'object_name': 'Picture'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'blank': 'True'})
        },
        'organisation.approval': {
            'Meta': {'object_name': 'Approval'},
            'approvalset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisation.ApprovalSet']"}),
            'approver': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Programmer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'organisation.approvalset': {
            'Meta': {'object_name': 'ApprovalSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['programming.Meeting']", 'unique': 'True'})
        },
        'programming.event': {
            'Meta': {'ordering': "['start']", 'object_name': 'Event'},
            'approval': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisation.Approval']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'default': "'<p>DEFAULT PLACEHOLDER TEXT</p>'", 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            'endTime': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 19, 10, 279000)'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fileupload.Picture']", 'null': 'True', 'blank': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'programmer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Programmer']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 12, 13, 0, 0)'}),
            'startTime': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 19, 10, 279000)'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'NEW EVENT'", 'max_length': '150'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'programming.festival': {
            'Meta': {'ordering': "['start']", 'object_name': 'Festival'},
            'approval': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisation.Approval']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'default': "'<p>DEFAULT PLACEHOLDER TEXT</p>'", 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            'endDate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 12, 13, 0, 0)'}),
            'endTime': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 19, 10, 280000)'}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['programming.Event']", 'symmetrical': 'False', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'films': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['programming.Film']", 'symmetrical': 'False', 'blank': 'True'}),
            'gigs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['programming.Gig']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fileupload.Picture']", 'null': 'True', 'blank': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'programmer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Programmer']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 12, 13, 0, 0)'}),
            'startTime': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 19, 10, 280000)'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'NEW FESTIVAL'", 'max_length': '150'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'programming.film': {
            'Meta': {'ordering': "['start']", 'object_name': 'Film'},
            'approval': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisation.Approval']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'default': "'<p>DEFAULT PLACEHOLDER TEXT</p>'", 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'certificate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Rating']"}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'filmFormat': ('django.db.models.fields.CharField', [], {'default': "'Unknown'", 'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'length': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fileupload.Picture']", 'null': 'True', 'blank': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'programmer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Programmer']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Season']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 12, 13, 0, 0)'}),
            'startTime': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 19, 10, 277000)'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'NEW FILM'", 'max_length': '150'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        'programming.gig': {
            'Meta': {'ordering': "['start']", 'object_name': 'Gig'},
            'approval': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisation.Approval']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'default': "'<p>DEFAULT PLACEHOLDER TEXT</p>'", 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end': ('django.db.models.fields.TimeField', [], {}),
            'endTime': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 19, 10, 278000)'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fileupload.Picture']", 'null': 'True', 'blank': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'programmer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Programmer']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 12, 13, 0, 0)'}),
            'startTime': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 19, 10, 278000)'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'NEW GIG'", 'max_length': '150'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'programming.meeting': {
            'Meta': {'ordering': "['start']", 'object_name': 'Meeting'},
            'approval': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisation.Approval']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'programmer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Programmer']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 12, 13, 0, 0)'}),
            'startTime': ('django.db.models.fields.TimeField', [], {'default': 'datetime.time(0, 19, 10, 282000)'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'General Meeting'", 'max_length': '150'})
        },
        'programming.programmer': {
            'Meta': {'ordering': "['name']", 'object_name': 'Programmer'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'homePhone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobilePhone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "'img/programmer/ron1-small.jpg'", 'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'programming.rating': {
            'Meta': {'ordering': "['name']", 'object_name': 'Rating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largeImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'smallImage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        'programming.season': {
            'Meta': {'ordering': "['start']", 'object_name': 'Season'},
            'approval': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['organisation.Approval']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'default': "'<p>DEFAULT PLACEHOLDER TEXT</p>'", 'blank': 'True'}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end': ('django.db.models.fields.DateField', [], {}),
            'endDate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 12, 13, 0, 0)'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'picture': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fileupload.Picture']", 'null': 'True', 'blank': 'True'}),
            'private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'programmer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programming.Programmer']"}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 12, 13, 0, 0)'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'NEW SEASON'", 'max_length': '150'})
        }
    }

    complete_apps = ['programming']