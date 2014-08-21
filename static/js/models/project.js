//  project.js
define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {
  
  var Project = Backbone.Model.extend({
    
    defaults: function() {
      return {
        name: '',
        location: '',
        landType: '',
        developer: '',
        landOwner: '',
        size: '',
        investmentGoal: 0,
        investmentCurrent: 0,
        investmentPercentage: 0,
        consumptionGoal: 0,
        consumptionCurrent: 0,
        consumptionPercentage: 0,
        endDate: '',
        schematicUrl: '',
        angleOfRoof: 0,
        sizeOfRoof: 0,
        numModules: 0,
        moduleWatts: 0,
        acPower: 0,
        annualPower: 0,
        powerDepreciation: 0.0025,
        co2Offset: 0,
        treesSaved: 0,
        milesDriven: 0,
        ytm: 0.07,
        greenCertificates: 0,
        payback: 0,
        cashflows: [],
        description: ''
      }
    }

  });

  return Project;

});