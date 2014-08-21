
define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {
  
  var UtilityCompany = Backbone.Model.extend({
    
    defaults: function() {
      return {
        name: 'name'
      }
    }

  });

  return UtilityCompany;

});