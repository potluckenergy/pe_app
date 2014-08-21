//  savingsView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/project/project-savings.html'
], function($, _, Backbone, template) {
  
  var SavingsView = Backbone.View.extend({

    template: _.template(template),

    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.html(this.template(this.model));
    }

  });

  return SavingsView;

});