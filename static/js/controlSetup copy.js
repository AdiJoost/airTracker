"use strict";

let get_control = function(name, color){
    let col = $.parseHTML('<div class="col-md-4 mt-3"></div>');
            let myButton = $.parseHTML('<button type="button"></button>');
                $(myButton).addClass(color)
                .addClass("btn w-100")
                .text(name)
                .attr("onclick", "send_shutdown()");
            $(col).append(myButton);
            

    return col;
}

let send_shutdown = function(){
    let baseUrl = window.location.origin;
    let myData = {
        "shutdown": true
    };
    $.ajax({
        type:"POST",
        url: baseUrl.concat("/nerveCenter"),
        data: myData,
        success: gotPost,
        dataType: "json",
        contetType: "application/json; charset=utf-8"
    });
}

let gotPost = function(result){
    alert(result);
}

jQuery.fn.controls = function(){
    let baseUrl = window.location.origin;

    let title = $.parseHTML("<h2>Controls</h2>");
    $(title).addClass("display-5 text-center my-4");
    $(this).append(title);

    
    let container = $.parseHTML("<div class='container'></div>");
        let row = $.parseHTML('<div class="row"></div>');  
            $(row).append(get_control("Shutdown", "btn-danger"));
        $(container).append(row);
    $(this).append(container);
    
    
    return this;
}