
define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {
  
  var Signup = Backbone.Model.extend({
    
    defaults: function() {
      return {
        name: 'name',
        email: 'email',
        zip: 'zip'
      }
    }

  });

  return Signup;

});