$(document).ready(function(){
    $("#nav-menu").click(function(){
        $("nav").toggleClass("show", "hide")
        if ($("nav").hasClass("show")) {
            $(".fa-chevron-down").css("transform", "rotate(180deg)")
        } else {
            $(".fa-chevron-down").css("transform", "rotate(0deg)")  
        }
    })
})