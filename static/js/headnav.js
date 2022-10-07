"use strict";

let get_navbutton = function(name, color, link){
    let col = $.parseHTML('<div class="col-md-3 mt-3"></div>');
            let myButton = $.parseHTML('<button type="button"></button>');
                $(myButton).addClass(color)
                .addClass("btn w-100")
                .text(name)
                .attr("onclick", "window.location=".concat("'",link, "'"));
            $(col).append(myButton);
            

    return col;
}

jQuery.fn.navigationBar = function(){
    let baseUrl = window.location.origin;

    let title = $.parseHTML("<h1>Air Tracker</h1>");
    $(title).addClass("display-3 text-center my-4");
    $(this).append(title);

    
    let container = $.parseHTML("<div class='container'></div>");
        let row = $.parseHTML('<div class="row"></div>');
            let col = $.parseHTML('<div class="col-md-3"></div>');
            $(row).append(get_navbutton("Home", "btn-primary", baseUrl.concat("/")));
            $(row).append(get_navbutton("Shutdown", "btn-danger", baseUrl.concat("/shutdown")));
            $(row).append(get_navbutton("About", "btn-info", baseUrl.concat("/")));
            $(row).append(get_navbutton("Spreadsheets", "btn-warning", baseUrl.concat("/")));
        $(container).append(row);
    $(this).append(container);
    console.log($(container));
    
    return this;
}

