//  headerView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/header.html',
  'text!templates/login.html',
  '../../../js/modules/modal'
], function($, _, Backbone, headerTemplate, loginTemplate, modal) {
  
  var HeaderView = Backbone.View.extend({
    
    el: $('#header'),

    //  render on initialization
    initialize: function() {
      this.render();
    },

    //  render template
    render: function() {
      this.$el.html(headerTemplate);
    },



    //
    //  Signup modal
    //
    events: {
      'click #login': 'login',
      //  'click #signup': 'signup',
      'click #open-nav': 'mobileNav',
      'click .mobile-link': 'mobileNav'
    },

    //
    //  Login modal
    //
    login: function() {
      modal.showLogin();
    },


    //
    //  Mobile nav
    //
    mobileNav: function() {
      $('.mobile-nav').slideToggle('fast');
    },

  });

  return HeaderView;

});