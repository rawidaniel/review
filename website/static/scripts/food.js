$(document).ready(() => {
    
    // This is to show the average rates of the foods
    $(".star-val").each(function(i, obj) {
        let starValEach = $(this).text()
        console.log(starValEach, i)
        //alert(starValEach, i)
        for (let i = 1; i < parseInt(starValEach) + 1; i++) {
                $(this).siblings(`#${i}`).css("color", "gold")
        }
        if (parseInt(starValEach) != parseFloat(starValEach)) {
            if (parseInt(starValEach) < parseFloat(starValEach)) {
                $(this).siblings(`#${parseInt(starValEach) + 1}`).removeClass("fa-star")
                $(this).siblings(`#${parseInt(starValEach) + 1}`).addClass("fa-star-half")
                $(this).siblings(`#${parseInt(starValEach) + 1}`).css("color", "gold")
            } else {
                $(this).siblings(`#${parseInt(starValEach) + 2}`).removeClass("fa-star")
                $(this).siblings(`#${parseInt(starValEach) + 2}`).addClass("fa-star-half")
                $(this).siblings(`#${parseInt(starValEach) + 2}`).css("color", "gold")
            }
        }
    });

    // This will listen to click events and go back to the previous page
    $("#go-back").click(function (){
        window.history.back();
    });
})