//  projectsView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/projects/projects.html',
  'views/projects/itemView',
  'collections/projects'
], function($, _, Backbone, template, ItemView, Projects) {
  
  var ProjectsView = Backbone.View.extend({

    el: $('#main'),

    template: _.template(template),

    projects: function() {
      var p = new Projects();
      $.getJSON(p.data, function(data) {
        $.each(data, function(item, val) {
          new ItemView({
            el: $('#projects-list'),
            model: val
          });
        });
      });
    },

    render: function() {
      this.$el.html(this.template);
      this.projects();
    }

  });

  return ProjectsView;

});