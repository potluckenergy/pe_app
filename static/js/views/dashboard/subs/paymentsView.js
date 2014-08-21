define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/dashboard/dashboard-payments.html'
], function($, _, Backbone, template) {
  
  var PaymentsView = Backbone.View.extend({

    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.html(template);
    }

  });

  return PaymentsView;

});