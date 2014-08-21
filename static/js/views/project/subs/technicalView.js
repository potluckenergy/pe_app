//  technicalView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'd3',
  'text!templates/project/project-technical.html',
  'text!templates/project/schematic.html',
  'modal'
], function($, _, Backbone, d3, template, schematicTemplate, modal) {
  
  var TechnicalView = Backbone.View.extend({

    template: _.template(template),

    production_data: [
      {year:1, value:158.0},
      {year:2, value:157.6},
      {year:3, value:157.2},
      {year:4, value:156.8},
      {year:5, value:156.4},
      {year:6, value:156.0},
      {year:7, value:155.6},
      {year:8, value:155.3},
      {year:9, value:154.9},
      {year:10, value:154.5},
      {year:11, value:154.1},
      {year:12, value:153.7},
      {year:13, value:153.3},
      {year:14, value:152.9},
      {year:15, value:152.6},
      {year:16, value:152.2},
      {year:17, value:151.8},
      {year:18, value:151.4},
      {year:19, value:151.0},
      {year:20, value:150.7}
    ],

    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.html(this.template(this.model));
      
      var schematic = this.model['schematicUrl'];

      //  Schematic
      $('#view-schematic').click( function() {
        modal.img(schematic);
      });

      //  d3
      d3.select('.production-chart')
        .selectAll('div')
          .data(this.production_data)
        .enter().append('div')
          .style('width', function(d){ return d.value * 3 + 'px' })
          .html(function(d){
            return '<span class="pull-left">'+d.year+'</span><span class="pull-right">'+d.value+'</span>'
          });
    }

  });

  return TechnicalView;

});