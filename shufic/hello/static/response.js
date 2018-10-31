jQuery("document").ready(function() {
    jQuery("#id_like").on('click',function () {
        var href = document.getElementById('id_like').name;
        console.log(href);
        jQuery.ajax({
            type:"GET",

            url: "/AllVideos/AddLike/ajax",

            data:{'addlike': href,},

            dataType: "text",

            catch: false,

            success: function (data){
               jQuery("#count_likes").html(data);
            }
        });
    });
});