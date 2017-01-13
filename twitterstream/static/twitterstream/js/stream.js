/**
 * Created by sammy on 12/7/16.
 */
(function(){
    var rqst = $.ajax({
        url: '/stream/streaming',
        data: {"N":"M"},
        type: 'post',
        datatype: 'json'
    });
    rqst.done(function(response){
        alert(response);
        var responseObj = $.parseJSON(response);

    });
}());