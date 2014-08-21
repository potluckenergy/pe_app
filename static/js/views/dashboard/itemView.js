//  itemView.js
//  /dashboard
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/dashboard/item.html'
], function($, _, Backbone, template) {
  
  var ItemView = Backbone.View.extend({

    template: _.template(template),

    render: function() {
      return this.template(this.model);
    }

  });

  return ItemView;

});