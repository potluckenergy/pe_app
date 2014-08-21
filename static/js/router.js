define([
  'jquery', 
  'underscore', 
  'backbone', 
  'views/header/headerView',
  'views/footer/footerView',
  'views/projects/projectsView',
  'views/dashboard/dashboardView',
  'views/project/projectView',
  'views/initiate/initiateView'
], function(
  $,
  _, 
  Backbone, 
  HeaderView,
  FooterView, 
  ProjectsView,
  DashboardView,
  ProjectView,
  InitiateView
) {
  
  var AppRouter = Backbone.Router.extend({
    routes: {
      'projects': 'projects',
      
      'project:id': 'project',
      'dashboard': 'dashboard',
      'initiate': 'initiate'
    },

    projects: function() {
      var projectsView = new ProjectsView();
      projectsView.render();
    },

    project: function(id) {
      var projectView = new ProjectView({id:id});
      projectView.render();
    },

    dashboard: function() {
      var dashboardView = new DashboardView();
      dashboardView.render();
    },

    initiate: function() {
      var initiateView = new InitiateView();
      initiateView.render();
    }

  });
  
  var initialize = function(){

    var router = new AppRouter;

    var headerView = new HeaderView();
    var footerView = new FooterView();

    Backbone.history.start({pushState: true}); 
  };

  return { 
    initialize: initialize
  };

});
