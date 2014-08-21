//  projectView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/project/project.html',
  'js/views/project/mainView.js',
  'collections/projects'
], function(
  $, 
  _, 
  Backbone,
  template,
  MainView,
  Projects
) {
  
  var ProjectView = Backbone.View.extend({
    
    el: $('#main'),

    projects: new Projects(),

    initialize: function(param) {
      this.id = String(param.id);
      this.render();
    },

    render: function() {
      var id = this.id;
      $.getJSON(this.projects.data, id, function(data) {
        new MainView({
          el: $('#main'),
          model: data[id]
        });
      });
    }

  });

  return ProjectView;

});