$(document).ready(function(){
$(".bbb").hide();
var urlHash = location.hash;
if(urlHash){
    $(".bbb").show();
}
$(".title").click(function(){
$(this).toggleClass("active").next().slideToggle("slow");
});
});

