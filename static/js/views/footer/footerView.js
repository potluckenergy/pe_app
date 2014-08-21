//  headerView.js
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/footer.html'
], function($, _, Backbone, footerTemplate, loginTemplate) {
  
  var FooterView = Backbone.View.extend({
    
    el: $('#footer'),

    //  render on initialization
    initialize: function() {
      this.render();
    },

    //  render template
    render: function() {
      this.$el.html(footerTemplate);
    }

  });

  return FooterView;

});