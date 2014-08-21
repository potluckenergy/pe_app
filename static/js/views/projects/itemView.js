//  itemView.js
//  /projects
define([
  'jquery',
  'underscore',
  'backbone',
  'text!templates/projects/item.html'
], function($, _, Backbone, template) {
  
  var ItemView = Backbone.View.extend({

    template: _.template(template),

    initialize: function() {
      this.render();
    },

    render: function() {
      this.$el.append(this.template(this.model));
    }

  });

  return ItemView;

});