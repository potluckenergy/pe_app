//  app.js
require.config({
  paths: {
    //  CDN
    'jquery': '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.min',
    'underscore': '//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.6.0/underscore-min',
    'backbone': '//cdnjs.cloudflare.com/ajax/libs/backbone.js/1.1.2/backbone-min',
    'text': '//cdnjs.cloudflare.com/ajax/libs/require-text/2.0.12/text',
    'd3': '//cdnjs.cloudflare.com/ajax/libs/d3/3.4.11/d3.min',
    'stripe': '//js.stripe.com/v2/',

    //  lib
    'firebase': 'lib/firebase.min',
    'backfire': 'lib/backbone-firebase.min',
    'chart': 'lib/column-chart',
    'templates': '../templates',
    
    //  modules
    'modal': 'modules/modal'
  }
});


//
//  pushState link config
//
require(['jquery', 'backbone'], function($, Backbone) {
  $(document.body).on('click', 'a', function(e){
    if ($(this).attr('href')!='/' && $(this).attr('href')!='/logout') {
      e.preventDefault();
    }
    Backbone.history.navigate(e.currentTarget.pathname, {trigger: true});
  });
});


//
//  initialize app router
//
require(['router'], function(Router) {
  Router.initialize();
});
