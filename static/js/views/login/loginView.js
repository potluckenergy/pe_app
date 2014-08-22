//  loginView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/login.html',
  'modal'
], function($, _, Backbone, loginTemplate, modal) {
  
  var LoginView = Backbone.View.extend({

    template: function() {
      return $('#login-template').html();
    },

    initialize: function() {
      this.render();
    },

    render: function() {
      modal.modal(this.template);
    }

  });

  return LoginView;

});