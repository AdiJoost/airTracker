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
    let thread_list = [["Mess-Sensor","measure_deamon"],
                        ["LED-Warnleuchte","led_deamon"],
                        ["Mail-Service","mail_deamon"],
                        ["Rebooter", "rebooter"]]

    let title = $.parseHTML("<h2>Controls</h2>");
    $(title).addClass("display-5 text-center my-4");
    $(this).append(title);

    
        let row = $.parseHTML('<div class="row"></div>');  
            for (const threadName of thread_list){
                let panel = $.parseHTML('<div class="col-md-4 mt-3"></div>');
                $(panel).threadPanel(threadName[0], threadName[1]);
                $(row).append(panel);
            }
    $(this).append(row);
    
    
    return this;
}