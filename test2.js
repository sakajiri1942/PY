$(document).ready(function(){
$(".acd-check3").hide();
$(".title").click(function(){
$(this).toggleClass("active").next().slideToggle("slow");
$(location.hash).find(".title").click();
});
});
