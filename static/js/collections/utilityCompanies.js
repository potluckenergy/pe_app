
define([
  'jquery',
  'underscore',
  'backbone',
  'firebase',
  'backfire',
  '../models/utilityCompany'
], function($, _, Backbone, Firebase, Backfire, UtilityCompany) {
  
  var UtilityCompanies = Backbone.Firebase.Collection.extend({
    
    model: UtilityCompany,

    firebase: 'https://potluck-energy.firebaseio.com/utility-companies'

  });

  return UtilityCompanies;

});