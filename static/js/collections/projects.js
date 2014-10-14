//  projects.js
define([
  'jquery',
  'underscore',
  'backbone',
  '../models/project'
], function($, _, Backbone, Project) {
  
  var Projects = Backbone.Collection.extend({

    model: Project,

    url: '/api/v1/project/?format=json'

  });

  return Projects;

});