let setPanel = function(result, threadKey){
    if (result["is_online"] == true){
        setPanelTrue(threadKey);
    } else {
        setPanelFalse(threadKey);
    }

}

let setPanelTrue = function(threadKey){
    $("#".concat(threadKey)).children().children(".alert")
    .removeClass(["alert-warning", "alert-danger"])
    .addClass("alert-success")
    .text("Online");

    $("#".concat(threadKey)).children().children(".btn")
    .removeClass("btn-outline-success")
    .addClass("btn-outline-danger")
    .text("Stop Deamon")
    .attr("onclick", 'stopDeamon("'.concat(threadKey).concat('")'));
}

let stopDeamon = function(threadKey){
    let baseUrl = window.location.origin;
    fetch(baseUrl.concat("/thread/").concat(threadKey),{
        method:"PUT",
        headers: {
            "Content-Type": "application/json"
        }
    }).then(response => {return response.json()})
    .then(body => setPanelFalse(threadKey))
    /*
    myOrder = JSON.stringify({"measure_deamon": {
                "shutdown": true
    }});
    const Http = new XMLHttpRequest();
    Http.open("PUT", baseUrl.concat("/nerveCenter"), true);
    Http.setRequestHeader("Content-Type", "application/json")
    Http.onreadystatechange = () =>{
        if(Http.readyState === XMLHttpRequest.DONE && Http.status === 200){
            setPanelFalse(threadKey)
        }
    }
    Http.send(myOrder);*/
}

let startDeamon = function(threadKey){
    let baseUrl = window.location.origin;
    fetch(baseUrl.concat("/thread/").concat(threadKey),{
        method:"POST"
    }).then(response => {return response.json()})
    .then(body => setPanelTrue(threadKey))
    /*
    myOrder = {"thread_name": threadKey};
    $.ajax({
        type:"POST",
        url: baseUrl.concat("/thread"),
        data: myOrder,
        success: function(result){
            setPanelTrue(threadKey);
        },
        dataType: "json",
        contetType: "application/json"
    })*/
}

let setPanelFalse = function(threadKey){
    $("#".concat(threadKey)).children().children(".alert")
    .removeClass(["alert-warning", "alert-success"])
    .addClass("alert-danger")
    .text("Offline");

    $("#".concat(threadKey)).children().children(".btn")
    .removeClass("btn-outline-danger")
    .addClass("btn-outline-success")
    .text("Start Deamon")
    .attr("onclick", 'startDeamon("'.concat(threadKey).concat('")'));
}



jQuery.fn.setStatus = function(threadKey){
    let baseUrl = window.location.origin;
    fetch(baseUrl.concat("/thread/").concat(threadKey),{
        method:"GET",
        headers: {
            "Content-Type": "application/json"
        },
        
    }).then(response => {return response.json()})
    .then(body => setPanel(body, threadKey))
    /*
    myData = {"thread_name": threadKey};
    $.ajax({
        type:"GET",
        url: baseUrl.concat("/thread"),
        data: myData,
        success: function(result){
            setPanel(result, threadKey);
        },
        dataType: "json",
        contetType: "application/json"
    })*/
    return this;
}


jQuery.fn.threadPanel = function(threadName, threadKey){
    let baseUrl = window.location.origin;

    let container = $.parseHTML('<div class="col-md-4 mt-3"></div>');
        let card = $.parseHTML('<div class="card text-center"></div>');
        $(card).attr("id", threadKey);
            let cardBody = $.parseHTML('<div class="card-body"></div>');
                let title = $.parseHTML('<h3 class="card-title"></h3>')
                $(title).text(threadName);
                $(cardBody).append(title);

                let status_request = $.parseHTML('<div class="alert alert-warning"></div>');
                $(status_request).text("Is Online?");
                $(cardBody).append(status_request);

                let action_button = $.parseHTML('<button class="btn"></button>');
                $(action_button).addClass(["btn-outline-danger", "w-100"]).text("Start Deamon");
                $(cardBody).append(action_button)
                $(cardBody).setStatus(threadKey)
            $(card).append(cardBody);
        $(this).append(card);

    
    
    return this;
}