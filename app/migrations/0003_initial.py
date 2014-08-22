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

        # Adding model 'Project'
        db.create_table(u'app_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acPower', self.gf('django.db.models.fields.IntegerField')()),
            ('angleOfRoof', self.gf('django.db.models.fields.IntegerField')()),
            ('annualPower', self.gf('django.db.models.fields.IntegerField')()),
            ('co2Offset', self.gf('django.db.models.fields.IntegerField')()),
            ('consumptionCurrent', self.gf('django.db.models.fields.IntegerField')()),
            ('consumptionGoal', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Developer'])),
            ('endDate', self.gf('django.db.models.fields.DateField')()),
            ('greenCertificates', self.gf('django.db.models.fields.IntegerField')()),
            ('investmentCurrent', self.gf('django.db.models.fields.IntegerField')()),
            ('investmentGoal', self.gf('django.db.models.fields.IntegerField')()),
            ('landOwner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.LandOwner'])),
            ('landType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.LandType'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('milesDriven', self.gf('django.db.models.fields.IntegerField')()),
            ('moduleWatts', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('numModules', self.gf('django.db.models.fields.IntegerField')()),
            ('payback', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('powerDepreciation', self.gf('django.db.models.fields.FloatField')()),
            ('schematicUrl', self.gf('django.db.models.fields.URLField')(max_length=500)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.IntegerField')()),
            ('treesSaved', self.gf('django.db.models.fields.IntegerField')()),
            ('ytm', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'app', ['Project'])


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

        # Deleting model 'Project'
        db.delete_table(u'app_project')


    models = {
        u'app.developer': {
            'Meta': {'object_name': 'Developer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'acPower': ('django.db.models.fields.IntegerField', [], {}),
            'angleOfRoof': ('django.db.models.fields.IntegerField', [], {}),
            'annualPower': ('django.db.models.fields.IntegerField', [], {}),
            'area': ('django.db.models.fields.IntegerField', [], {}),
            'co2Offset': ('django.db.models.fields.IntegerField', [], {}),
            'consumptionCurrent': ('django.db.models.fields.IntegerField', [], {}),
            'consumptionGoal': ('django.db.models.fields.IntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Developer']"}),
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'greenCertificates': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'investmentCurrent': ('django.db.models.fields.IntegerField', [], {}),
            'investmentGoal': ('django.db.models.fields.IntegerField', [], {}),
            'landOwner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.LandOwner']"}),
            'landType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.LandType']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'milesDriven': ('django.db.models.fields.IntegerField', [], {}),
            'moduleWatts': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'numModules': ('django.db.models.fields.IntegerField', [], {}),
            'payback': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'powerDepreciation': ('django.db.models.fields.FloatField', [], {}),
            'schematicUrl': ('django.db.models.fields.URLField', [], {'max_length': '500'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'treesSaved': ('django.db.models.fields.IntegerField', [], {}),
            'ytm': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        }
    }

    complete_apps = ['app']