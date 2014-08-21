//  environmentalView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/project/project-environmental.html'
], function($, _, Backbone, template) {
  
  var EnvironmentalView = Backbone.View.extend({

    template: _.template(template),

    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.html(this.template(this.model));
      
      //  render trees
      var counter = this.model['treesSaved'];
      while ( counter > 0 ) {
        $('.trees').append('<i class="fa fa-tree"></i>');
        counter = counter - 1;
      }

      //  render cars
      counter = this.model['milesDriven'];
      while ( counter > 0 ) {
        $('.cars').append('<i class="fa fa-car"></i>');
        counter = counter - 1;
      }
    }

  });

  return EnvironmentalView;

});