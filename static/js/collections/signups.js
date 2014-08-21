
define([
  'jquery',
  'underscore',
  'backbone',
  'firebase',
  'backfire',
  '../models/signup'
], function($, _, Backbone, Firebase, Backfire, Signup) {
  
  var Signups = Backbone.Firebase.Collection.extend({
    
    model: Signup,

    firebase: 'https://potluck-energy.firebaseio.com/signups'

  });

  return Signups;

});