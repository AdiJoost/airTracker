let getCo2 = function(){
    let baseUrl = window.location.origin;
    fetch(baseUrl.concat("/nerveCenter"))
    .then(response => {return response.json()})
    .then(body => insertCo2(body));
}

let insertCo2 = function(body){
    $("#co2Title").text("CO2: "
    .concat(body["co2"])
    .concat(" ppm"));
    setTimeout(getCo2, 15000)
}

let getText = function(){
    let description = `
    <p class="lead">Here is what that means...</p>
    `
    return description;
}

jQuery.fn.co2Display = function(){
    let baseUrl = window.location.origin;
    let jumbotron = $.parseHTML("<div></div>");
    $(jumbotron).addClass(["mt-4",
                            "text-center",
                            "bg-primary",
                            "text-white",
                            "rounded",
                            "p-3"]);
        let title = $.parseHTML("<div>Your co2 is</div>");
        $(title).addClass(["display-4", "mt-3"]).attr("id", "co2Title");
        getCo2();
        
        let text = $.parseHTML(getText());
        $(jumbotron).append(title);
        $(jumbotron).append($.parseHTML("<hr>"));
        $(jumbotron).append(text);

    
    $(this).append(jumbotron);
    return this;
}