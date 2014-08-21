
define([
  'jquery',
  'underscore',
  'backbone',
  'views/dashboard/itemView'
], function($, _, Backbone, ItemView) {
  
  var ListView = Backbone.View.extend({

    render: function() {
      var element = this.$el;

      //  loop through collection...
      this.collection.forEach( function(item) {
        //  ...rendering itemView for each item
        element.append( new ItemView({model: item}).render() );
      });
    }

  });

  return ListView;

});