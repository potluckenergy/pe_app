define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/dashboard/dashboard-investments.html'
], function($, _, Backbone, template) {
  
  var InvestmentsView = Backbone.View.extend({

    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.html(template);
    }

  });

  return InvestmentsView;

});