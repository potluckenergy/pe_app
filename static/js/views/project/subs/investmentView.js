//  investmentView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'd3',
  'chart',
  'text!templates/project/project-investment.html'
], function($, _, Backbone, d3, chart, template) {
  
  var InvestmentView = Backbone.View.extend({

    template: _.template(template),

    cf_data: [
      [0,-100000],
      [1,4000],
      [2,4000],
      [3,4000],
      [4,4000],
      [5, 4000],
      [6,4000],
      [7,4000],
      [8,4000],
      [9,4000],
      [10, 4000],
      [11,4000],
      [12,4000],
      [13,4000],
      [14,4000],
      [15, 4000],
      [16,4000],
      [17,4000],
      [18,4000],
      [19,4000],
      [20, 4000]
    ],

    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.html(this.template(this.model));
      
      //  Cash flow chart
      d3.select(".cf-chart")
        .datum(this.cf_data)
          .call(columnChart()
            .width(600)
            .height(400)
            .x(function(d, i) { return d[0]; })
            .y(function(d, i) { return d[1]; }));

      $('svg').css('width', '100%');
    }

  });

  return InvestmentView;

});