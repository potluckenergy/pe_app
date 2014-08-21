//  loadZone.js
define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {
  
  var LoadZone = Backbone.Model.extend({
    
    defaults: function() {
      return {
        name: 'name'
      }
    }

  });

  return LoadZone;

});