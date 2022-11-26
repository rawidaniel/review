$(document).ready(function(){
    $("#menu").click(function(){
        $("nav").toggleClass("show", "hide")
        if ($("nav").hasClass("show")) {
            $("#menu").empty().html('<li><i class="fa-solid fa-x"></i></li>')
        } else {
            $("#menu").empty().html('<li><i class="fa-solid fa-bars"></i></li>')
            
        }
    })
})