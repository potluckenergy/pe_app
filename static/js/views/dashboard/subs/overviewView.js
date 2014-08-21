define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/dashboard/dashboard-overview.html'
], function($, _, Backbone, template) {
  
  var OverviewView = Backbone.View.extend({

    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.html(template);
    }

  });

  return OverviewView;

});