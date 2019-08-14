$(document).ready(function() {

    $("#search").click(function() {
        var searchReq = $.get("/sendRequest/" + $("#query"_.val());
        searchReq.done(function(data) {
            $("#url").attr("href", data.result);
        });
    });
    
});