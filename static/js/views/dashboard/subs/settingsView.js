define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/dashboard/dashboard-settings.html'
], function($, _, Backbone, template) {
  
  var SettingsView = Backbone.View.extend({

    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.html(template);
    }

  });

  return SettingsView;

});