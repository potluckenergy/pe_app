//  projects.js
define([
  'jquery',
  'underscore',
  'backbone',
  'firebase',
  'backfire',
  '../models/project'
], function($, _, Backbone, Firebase, Backfire, Project) {
  
  var Projects = Backbone.Firebase.Collection.extend({

    model: Project,

    firebase: 'https://potluck-energy.firebaseio.com/projects',

    data: 'https://potluck-energy.firebaseio.com/projects.json'

  });

  return Projects;

});