define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/dashboard/dashboard-manage.html',
  'collections/loadZones',
  'collections/townships',
  'collections/utilityCompanies',
  'views/dashboard/listView'
], function($, _, Backbone, template, LoadZones, Townships, UtilityCompanies, ListView) {
  
  var ManageView = Backbone.View.extend({

    //
    //  Events
    //
    events: {
      'click #new-load-zone': 'newLoadZone',
      'click #new-township': 'newTownship',
      'click #new-utility-company': 'newUtilityCompany',
      'click #add-load-zone': 'addLoadZone',
      'click #add-township': 'addTownship',
      'click #add-utility-company': 'addUtilityCompany'
    },

    //
    //  Toggle 'add new ...'
    //
    newLoadZone: function() { $('.new-load-zone').slideToggle(); },
    newTownship: function() { $('.new-township').slideToggle(); },
    newUtilityCompany: function() { $('.new-utility-company').slideToggle(); },

    //
    //  Add new load zone
    //
    loadZones: new LoadZones(),
    addLoadZone: function() {
      this.loadZones.create({ name: $('#load-zone-name').val() });
      this.render();
    },

    //
    //  Add new township
    //
    townships: new Townships(),
    addTownship: function() {
      this.townships.create({ name: $('#township-name').val() });
      this.render();
    },

    //
    //  Add new utility company
    //
    utilityCompanies: new UtilityCompanies(),
    addUtilityCompany: function() {
      this.utilityCompanies.create({ name: $('#utility-company-name').val() });
      this.render();
    },


    //
    //  Init
    //
    initialize: function() {
      this.render();
    },


    //
    //  Render.
    //  - called initiallly, then each time an 'add' event is triggered
    //
    render: function() {
      this.$el.html(template);

      //
      //  Render ListViews
      //
      
      //  Load zones
      new ListView({
        collection: this.loadZones.toJSON(),
        el: $('.list-load-zones')
      }).render();

      //  Townships
      new ListView({
        collection: this.townships.toJSON(),
        el: $('.list-townships')
      }).render();

      //  Utility Companies
      new ListView({
        collection: this.utilityCompanies.toJSON(),
        el: $('.list-utility-companies')
      }).render();
    }

  });

  return ManageView;

});