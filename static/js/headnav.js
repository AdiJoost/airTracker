"use strict";

jQuery.fn.navigationBar = function(){
    let baseUrl = window.location.origin;

    let title = $.parseHTML("<h1>Air Tracker</h1>");
    $(title).addClass("display-3 text-center my-4")
    $(this).append(title);

    return this;
}