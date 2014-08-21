
define([
  'jquery',
  'underscore',
  'backbone',
  'firebase',
  'backfire',
  '../models/township'
], function($, _, Backbone, Firebase, Backfire, Township) {
  
  var Townships = Backbone.Firebase.Collection.extend({
    
    model: Township,

    firebase: 'https://potluck-energy.firebaseio.com/townships'

  });

  return Townships;

});