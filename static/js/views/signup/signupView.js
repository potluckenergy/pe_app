//  signupView.js
define([
  'jquery',
  'underscore',
  'backbone',
  '../../models/signup',
  '../../collections/signups',
  'text!templates/signup.html'
], function($, _, Backbone, Signup, Signups, signupTemplate) {

  var SignupView = Backbone.View.extend({

    el: $('.mailing-list'),

    events: {
      'click #do-signup': 'doSignup'
    },

    doSignup: function() {

      var name = $('#signup-name').val();
      var email = $('#signup-email').val();
      var zip = $('#signup-zip').val();

      var user = {
        name: name,
        email: email,
        zip: zip
      }
      if (name != '' && email != '' && zip != '') {
        this.signups.add(user);
        $('.signup-form').fadeOut('fast');
        setTimeout( function(){
          $('.thanks-signup').fadeIn('fast');
        }, 500);
        
      }
      

    },

    initialize: function() {
      this.render();
      this.signups = new Signups();
    },

    render: function() {
      this.$el.html( signupTemplate );
    }

  });

  return SignupView;

});