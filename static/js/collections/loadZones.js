//  loadZones.js
define([
  'jquery',
  'underscore',
  'backbone',
  'firebase',
  'backfire',
  '../models/loadZone'
], function($, _, Backbone, Firebase, Backfire, LoadZone) {
  
  var LoadZones = Backbone.Firebase.Collection.extend({
    
    model: LoadZone,

    firebase: 'https://potluck-energy.firebaseio.com/load-zones'

  });

  return LoadZones;

});