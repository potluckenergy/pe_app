# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UtilityCompany'
        db.create_table(u'app_utilitycompany', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'app', ['UtilityCompany'])

        # Adding model 'LoadZone'
        db.create_table(u'app_loadzone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'app', ['LoadZone'])

        # Adding model 'Township'
        db.create_table(u'app_township', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('loadZone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.LoadZone'])),
        ))
        db.send_create_signal(u'app', ['Township'])

        # Adding model 'Developer'
        db.create_table(u'app_developer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'app', ['Developer'])

        # Adding model 'LandOwner'
        db.create_table(u'app_landowner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'app', ['LandOwner'])

        # Adding model 'LandType'
        db.create_table(u'app_landtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'app', ['LandType'])

        # Adding model 'Settings'
        db.create_table(u'app_settings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('township', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Township'], blank=True)),
        ))
        db.send_create_signal(u'app', ['Settings'])

        # Adding model 'Project'
        db.create_table(u'app_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acPower', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('angleOfRoof', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('annualPower', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('co2Offset', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('consumptionCurrent', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('consumptionGoal', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Developer'], blank=True)),
            ('endDate', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('greenCertificates', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('investmentCurrent', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('investmentGoal', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('landOwner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.LandOwner'], blank=True)),
            ('landType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.LandType'], blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('milesDriven', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('moduleWatts', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('numModules', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('payback', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('powerDepreciation', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('schematicUrl', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('area', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('treesSaved', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('ytm', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'app', ['Project'])

        # Adding model 'Investment'
        db.create_table(u'app_investment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Project'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Investment'])

        # Adding model 'Consumption'
        db.create_table(u'app_consumption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Project'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'app', ['Consumption'])


    def backwards(self, orm):
        # Deleting model 'UtilityCompany'
        db.delete_table(u'app_utilitycompany')

        # Deleting model 'LoadZone'
        db.delete_table(u'app_loadzone')

        # Deleting model 'Township'
        db.delete_table(u'app_township')

        # Deleting model 'Developer'
        db.delete_table(u'app_developer')

        # Deleting model 'LandOwner'
        db.delete_table(u'app_landowner')

        # Deleting model 'LandType'
        db.delete_table(u'app_landtype')

        # Deleting model 'Settings'
        db.delete_table(u'app_settings')

        # Deleting model 'Project'
        db.delete_table(u'app_project')

        # Deleting model 'Investment'
        db.delete_table(u'app_investment')

        # Deleting model 'Consumption'
        db.delete_table(u'app_consumption')


    models = {
        u'app.consumption': {
            'Meta': {'object_name': 'Consumption'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Project']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'app.developer': {
            'Meta': {'object_name': 'Developer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'app.investment': {
            'Meta': {'object_name': 'Investment'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Project']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'app.landowner': {
            'Meta': {'object_name': 'LandOwner'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'app.landtype': {
            'Meta': {'object_name': 'LandType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'app.loadzone': {
            'Meta': {'object_name': 'LoadZone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'app.project': {
            'Meta': {'object_name': 'Project'},
            'acPower': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'angleOfRoof': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'annualPower': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'area': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'co2Offset': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'consumptionCurrent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'consumptionGoal': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Developer']", 'blank': 'True'}),
            'endDate': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'greenCertificates': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investmentCurrent': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'investmentGoal': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'landOwner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.LandOwner']", 'blank': 'True'}),
            'landType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.LandType']", 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'milesDriven': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'moduleWatts': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'numModules': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'payback': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'powerDepreciation': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'schematicUrl': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'treesSaved': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'ytm': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'app.settings': {
            'Meta': {'object_name': 'Settings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'township': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Township']", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'app.township': {
            'Meta': {'object_name': 'Township'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loadZone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.LoadZone']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'app.utilitycompany': {
            'Meta': {'object_name': 'UtilityCompany'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']