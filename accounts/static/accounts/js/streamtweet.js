/**
 * Created by sammy on 11/25/16.
 */
// setInterval(function(){
//     var srvRqst = $.ajax({
//             url: '/stream/streaming/',
//             data: {},
//             type: 'post',
//             datatype: 'application/json'
//         });
//     srvRqst.done(function(response){
//         var tweets = response;
//         $('.done').html(tweets).fadeIn('slow');
//         document.getElementById("demo").innerHTML = tweets
//         /*alert(JSON.stringify(tweets));*/
//         for(var i = 0; i< tweets.length; i++ ){
//                 var author = tweets[i]['author'];
//         }
//     });
// }, 2000);


setInterval(function(){
var srvRqst = $.ajax({
        url: '/stream/streaming/',
        data: {},
        type: 'post',
        datatype: 'application/json'
    });
srvRqst.done(function(response){
    var tweets =  response;

    //$('.done').html(tweets).fadeIn('slow');
    //console.log(tweets['data']);
    for(var i=0; i< tweets['data'].length; i++){
       var data = $.parseJSON(tweets['data']);
        console.log(data[0]['fields']['text']);

     $("#demo").append(data[0]['fields']['text']+"<br>");
    }


//         /*alert(JSON.stringify(tweets));*/
// {#        for(var i = 0; i< tweets.length; i++ ){#}
// {#                document.getElementById("demo").innerHTML = tweets.pk;#}
// {#        }#}
    });
}, 2000);


    // using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
