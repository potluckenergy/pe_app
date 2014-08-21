//  loginView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/login.html',
  'modal'
], function($, _, Backbone, loginTemplate, modal) {
  
  var LoginView = Backbone.View.extend({

    initialize: function() {
      this.render();
    },

    render: function() {
      modal.modal(loginTemplate);
    }

  });

  return LoginView;

});