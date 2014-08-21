//  mainView.js
//  /project
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/project/main.html',
  'js/views/project/subs/overviewView.js',
  'js/views/project/subs/technicalView.js',
  'js/views/project/subs/environmentalView.js',
  'js/views/project/subs/investmentView.js',
  'js/views/project/subs/savingsView.js'
], function(
  $, 
  _, 
  Backbone, 
  template,
  OverviewView,
  TechnicalView,
  EnvironmentalView,
  InvestmentView,
  SavingsView
) {
  
  var MainView = Backbone.View.extend({

    template: _.template(template),

    events: {
      'click #select-overview': 'overview',
      'click #select-technical': 'technical',
      'click #select-environmental': 'environmental',
      'click #select-investment': 'investment',
      'click #select-savings': 'savings'
    },
    

    //
    //  Overview
    //
    overview: function() {
      $('.tab').each( function() {
        $(this).removeClass('current');
      });
      $('#select-overview').parent('li').addClass('current');
      new OverviewView({
        el: $('#project-content'),
        model: this.model
      });
    },

    
    //
    //  Technical
    //
    technical: function() {
      $('.tab').each( function() {
        $(this).removeClass('current');
      });
      $('#select-technical').parent('li').addClass('current');
      new TechnicalView({
        el: $('#project-content'),
        model: this.model
      });
    },


    //
    //  Environmental
    //
    environmental: function() {
      $('.tab').each( function() {
        $(this).removeClass('current');
      });
      $('#select-environmental').parent('li').addClass('current');
      new EnvironmentalView({
        el: $('#project-content'),
        model: this.model
      });
    },


    //
    //  Investment
    //
    investment: function() {
      $('.tab').each( function() {
        $(this).removeClass('current');
      });
      $('#select-investment').parent('li').addClass('current');
      new InvestmentView({
        el: $('#project-content'),
        model: this.model
      });
    },


    //
    //  Savings
    //
    savings: function() {
      $('.tab').each( function() {
        $(this).removeClass('current');
      });
      $('#select-savings').parent('li').addClass('current');
      new SavingsView({
        el: $('#project-content'),
        model: this.model
      });
    },




    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.html(this.template(this.model));
      this.overview();
    }

  });

  return MainView;

});