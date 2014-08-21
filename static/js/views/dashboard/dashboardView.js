//  dashboardView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/dashboard/dashboard.html',
  'js/views/dashboard/subs/overviewView.js',
  'js/views/dashboard/subs/paymentsView.js',
  'js/views/dashboard/subs/investmentsView.js',
  'js/views/dashboard/subs/settingsView.js',
  'js/views/dashboard/subs/manageView.js',
], function(
  $, 
  _, 
  Backbone,
  dashboardTemplate,
  OverviewView,
  PaymentsView,
  InvestmentsView,
  SettingsView,
  ManageView
) {
  
  var DashboardView = Backbone.View.extend({
    
    el: $('#main'),


    events: {
      'click #select-overview': 'selectOverview',
      'click #select-payments': 'selectPayments',
      'click #select-investments': 'selectInvestments',
      'click #select-settings': 'selectSettings',
      'click #select-manage': 'selectManage'
    },



    selectOverview: function() {
      $('.list-item').each( function() {
        $(this).removeClass('current');
      });
      $('#select-overview').parent('li').addClass('current');

      new OverviewView({ el: $('#dashboard-content') });
    },

    selectPayments: function() {
      $('.list-item').each( function() {
        $(this).removeClass('current');
      });
      $('#select-payments').parent('li').addClass('current');
      $('#dashboard-section').html('Payments');

      new PaymentsView({ el: $('#dashboard-content') });
    },

    selectInvestments: function() {
      $('.list-item').each( function() {
        $(this).removeClass('current');
      });
      $('#select-investments').parent('li').addClass('current');
      $('#dashboard-section').html('Investments');

      new InvestmentsView({ el: $('#dashboard-content') });
    },

    selectSettings: function() {
      $('.list-item').each( function() {
        $(this).removeClass('current');
      });
      $('#select-settings').parent('li').addClass('current');
      $('#dashboard-section').html('Settings');

      new SettingsView({ el: $('#dashboard-content') });
    },

    selectManage: function() {
      $('.list-item').each( function() {
        $(this).removeClass('current');
      });
      $('#select-manage').parent('li').addClass('current');
      $('#dashboard-section').html('Manage');

      new ManageView({ el: $('#dashboard-content') });
    },

    render: function() {
      this.$el.html(dashboardTemplate);
      this.selectOverview();
    }

  });

  return DashboardView;

});