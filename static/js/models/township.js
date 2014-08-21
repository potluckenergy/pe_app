
define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {
  
  var Township = Backbone.Model.extend({
    
    defaults: function() {
      return {
        name: 'name'
      }
    }

  });

  return Township;

});