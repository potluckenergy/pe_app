//  initiateView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/initiate.html',
  'collections/projects'
], function($, _, Backbone, template, Projects) {
  
  var InitiateView = Backbone.View.extend({

    el: $('#main'),

    events: {
      'click #initiate-project': 'initiateProject'
    },

    projects: new Projects(),
    initiateProject: function() {
      this.projects.create({
        name: $('#project-name').val(),
        location: $('#project-location').val(),
        landType: $('#project-land-type').val(),
        developer: $('#project-developer').val(),
        landOwner: $('#project-land-owner').val(),
        size: $('#project-size').val(),
        investmentGoal: $('#project-investment-goal').val(),
        //  investmentCurrent: 0,
        consumptionGoal: $('#project-consumption-goal').val(),
        //  consumptionCurrent: 0,
        endDate: $('#project-end-date').val(),
        schematicUrl: $('#project-schematic-url').val(),
        angleOfRoof: $('#project-roof-angle').val(),
        sizeOfRoof: $('#project-area').val(),
        numModules: $('#project-num-modules').val(),
        moduleWatts: $('#project-modules-watts').val(),
        acPower: $('#project-ac-power').val(),
        annualPower: $('#project-annual-power').val(),
        //  powerDepreciation: 0.0025,
        //  co2Offset: $('#project-co2-offset').val(),
        //  treesSaved: $('#project-trees-saved').val(),
        //  milesDriven: $('#project-miles-driven').val(),
        //  ytm: 0.07,
        //  greenCertificates: $('#project-green-certificates').val(),
        //  payback: $('#project-payback').val(),
        //  cashflows: 'array',
        description: $('#project-description').val()
      });
    },

    render: function() {
      this.$el.html(template);
    }

  });

  return InitiateView;

});