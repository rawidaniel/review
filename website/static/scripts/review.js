$(document).ready(() => {

    let userId = $("input[type='hidden']").attr("data-user-id")
    let foodId = $("input[type='hidden']").attr("data-food-id")
    console.log(userId, foodId)
    let reviewId;
    let starSet;
    let textSet;


// Get rate and review from backend and put it on user page
    $("body").css("opacity", "0")
    fetch('http://18.205.104.232:5001/api/v1/foods/' + foodId + '/reviews')
   .then(response => {
    if (response.status == 404) {
        alert(`You are not connected to the internet ! ${error}`)
        alert(`Failed to load your data! Reloading your page in 3 seconds `)
        console.log(error)
        $("body").empty().text("FAILED TO LOAD THE DATA ! :(  ... RELOAD MANUALLY").css("color", "red")
        console.log("404 Status code!!! Reload Manually")
        $("body").css("opacity", "1")
    } else {
        return response.json()
    }
   })
   .then(data => {
    let infoData = JSON.stringify(data)
    let dataObject = JSON.parse(infoData)

    for (let i = 0; i < dataObject.length; i++) {
        console.log(dataObject)
        if (dataObject[i].user_id == userId) {
            reviewId = dataObject[i].id;
            $("input[type='hidden']").attr("data-review-id", reviewId)
            console.log(`reviewId is ${reviewId}`, `To be sure ${$("input[type='hidden']").attr("data-review-id")}`)
            starSet = parseInt(dataObject[i].rate);
            console.log(starSet, typeof(starSet))
            textSet = dataObject[i].text
            console.log(textSet, typeof(textSet))
        }
    }

    if ((starSet > 0) && ((starSet != null) || (starSet != NaN))) {
        $(".star-val").text(starSet)
        $(".fa-solid").mouseleave()
      }

      if ((textSet != "") && (textSet != null)) {
        $(".this-usr-comment").text(textSet);
        $(".btn-outline-success").text("Edit");
        $(".btn-outline-danger").text("Delete");
        $(".btn-outline-primary").prop("disabled", true)
        $(".btn-outline-primary").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
        $("#input").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
      } else {
        $(".btn-outline-primary").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
        $("#input").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
        $(".usr-comment").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
      }
      $("body").css("opacity", "1")
      console.log("Page load success")
   })
   .catch(error => {
    alert(`You are not connected to the internet ! ${error}`)
    alert(`Failed to load your data! Reloading your page in 3 seconds `)
    console.log(error)
    $("body").empty().text("FAILED TO LOAD THE DATA ! :(  ... RELOAD MANUALLY").css("color", "red")
    console.log("error caught!!! Reload Manually")
    $("body").css("opacity", "1")
   });


// Listen to key press and make post button appear
   $("#input").keypress(function(){
        //$(this).siblings(".btn-outline-primary").css("visibility", "visible")
        $(".btn-outline-primary").css("visibility", "visible").css("height", "auto").css("width", "auto").css("padding", "10px").css("margin", "10px")
        //$("#input").css("visibility", "hidden").css("height", "100px").css("width", "80%")
    })


// Listen to click events and post it on user page and send it to back
    $(".btn-outline-primary").click(function(){
        $("#loading-cmt").empty().html('<div class="spinner-border text-primary" \
        role="status"><span class="visually-hidden">Loading...</span></div>')
        let textVal = $(this).siblings("#input").val()
        console.log(textVal)
        /*
        let userId = $("input[type='hidden']").attr("data-user-id")
        let foodId = $("input[type='hidden']").attr("data-food-id")
        */
       if (reviewId == null) {
        let reviewId = $("input[type='hidden']").attr("data-review-id")
       }
        
        if ((reviewId == null) || (reviewId == "")) {
            console.log("POST method used")
            $.ajax({
                type: 'POST',
                url: "http://18.205.104.232:5001/api/v1/foods/" + foodId +"/reviews",
                headers: {
                    'Content-Type': 'application/json'
                },
                data: JSON.stringify({
                    text: textVal,
                    user_id: userId,
                    rate: 0
                }),
                success: function(response){
                    console.log(response)
                    $("#input").val("")
                    $(".this-usr-comment").text(textVal);
                    $(".btn-outline-success").text("Edit");
                    $(".btn-outline-danger").text("Delete");
                    $(".btn-outline-primary").prop("disabled", true)
                    $("#alert-user").empty().html('<div class="alert alert-success" \
                    role="alert">You reviewed this food successfully!</div>')
                    $("#loading-cmt").empty()
                    $(".btn-outline-primary").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
                    $("#input").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
                    $(".usr-comment").css("visibility", "visible").css("height", "auto").css("width", "auto").css("padding", "auto").css("margin", "auto")
                    const myTimeout = setTimeout(clearAlert, 3000);
                    console.log(JSON.parse(response))
                    resObject = JSON.parse(response)
                    reviewId = resObject.id
                    console.log(reviewId)
                    $("input[type='hidden']").attr("data-review-id", resObject.id)
                    
    
                },
                error: function(error){
                    console.log(error);
                    alert("You are not connected to the internet ! ", error)
                    $("#loading-cmt").empty()
                }
            });
        } else {
            console.log("PUT method used")
            $.ajax({
                type: 'PUT',
                url: "http://18.205.104.232:5001/api/v1/reviews/" + reviewId,
                headers: {
                    'Content-Type': 'application/json'
                },
                data: JSON.stringify({
                    text: textVal,
                    user_id: userId,
                }),
                success: function(response){
                    console.log(response)
                    $("#input").val("")
                    $(".this-usr-comment").text(textVal);
                    $(".btn-outline-success").text("Edit");
                    $(".btn-outline-danger").text("Delete");
                    $(".btn-outline-primary").prop("disabled", true)
                    $("#alert-user").empty().html('<div class="alert alert-success" \
                    role="alert">You reviewed this food successfully!</div>')
                    $("#loading-cmt").empty()
                    $(".btn-outline-primary").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
                    $("#input").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
                    $(".usr-comment").css("visibility", "visible").css("height", "auto").css("width", "auto").css("padding", "auto").css("margin", "auto")
                    const myTimeout = setTimeout(clearAlert, 3000);
                    
    
                },
                error: function(error){
                    console.log(error);
                    alert("You are not connected to the internet ! ", error)
                    $("#loading-cmt").empty()
                }
            });
        }
        
    })


// Detect if edit button is clicked and makes the text editable
    $("#edit").click(function(){
        let textVal = $(".this-usr-comment").text()

        $("#input").val(textVal)
        $(".btn-outline-primary").prop("disabled", false)
        $(".btn-outline-primary").css("visibility", "visible").css("height", "auto").css("width", "auto").css("padding", "10px").css("margin", "10px")
        $("#input").css("visibility", "visible").css("height", "100px").css("width", "80%").css("padding", "auto").css("margin", "25px auto")
        $('input').focus();
    })


// Detect if delete button is clicked and delete the text on the user page and send delete req to back
    $("#delete").click(function(){
        $("#loading-dlt").empty().html('<div class="spinner-border text-danger" \
        role="status"><span class="visually-hidden">Loading...</span></div>')
        /*
        let userId = $("input[type='hidden']").attr("data-user-id")
        let foodId = $("input[type='hidden']").attr("data-food-id")
        */
       let textVal = ""
       console.log("partial DELETE method used")
        $.ajax({
            type: 'PUT',
            url: "http://18.205.104.232:5001/api/v1/reviews/" + reviewId,
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({
                user_id: userId,
                text: textVal
            }),
            success: function(response){
                console.log(response)
                $(".this-usr-comment").text("")
                $("#edit").text("")
                $("#delete").text("")
                $(".btn-outline-primary").prop("disabled", false)
                $("#alert-user").empty().html('<div class="alert alert-danger"\
                 role="alert">Your review is deleted !</div>')
                 $("#loading-dlt").empty()
                 $(".usr-comment").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
                 const myTimeout = setTimeout(clearAlert, 3000);
            },
            error: function(error){
                console.log(error);
                alert("You are not connected to the internet !", error)
                $("#loading-dlt").empty()
            }
        });
        
    })


// This sets the average rate value for the selected food
    $(".star-val-noedit").each(function(i, obj) {
        let starValEach = $(this).text()
        //console.log(starValEach, i)
        for (let i = 1; i < parseInt(starValEach) + 1; i++) {
                $(this).siblings(`#${i}`).css("color", "rgb(247, 184, 14)")
        }
        if (parseInt(starValEach) != parseFloat(starValEach)) {
            if (parseInt(starValEach) < parseFloat(starValEach)) {
                $(this).siblings(`#${parseInt(starValEach) + 1}`).removeClass("fa-star")
                $(this).siblings(`#${parseInt(starValEach) + 1}`).addClass("fa-star-half")
                $(this).siblings(`#${parseInt(starValEach) + 1}`).css("color", "rgb(247, 184, 14)")
            } else {
                $(this).siblings(`#${parseInt(starValEach) + 2}`).removeClass("fa-star")
                $(this).siblings(`#${parseInt(starValEach) + 2}`).addClass("fa-star-half")
                $(this).siblings(`#${parseInt(starValEach) + 2}`).css("color", "rgb(247, 184, 14)")
            }
        }
    });
    

// This function copies the clicked text, the contact number or the address of the restaurant to the clipbord
    $(".fa-copy").click(function(){
        var copyText = $(this).siblings("span").text();
        navigator.permissions.query({ name: "clipboard-write" }).then((result) => {
            if (result.state == "granted" || result.state == "prompt") {
              alert("Write access ranted!");
            }
          });
        navigator.clipboard.writeText(copyText).then(() => {
            alert(`Copied to clipboard: ${copyText}`);
        });
    });



// This is for the review input pop up function
$('.btn-link').click(function(){
    //$(this).siblings("input").css("animation-play-state", "running")  
    $(".btn-outline-primary").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "auto").css("margin", "auto")
    $("#input").css("visibility", "visible").css("height", "100px").css("width", "80%").css("padding", "auto").css("margin", "auto")
})


 //Bind keypress event to input element
 $('#input').keypress(function(event){
    var keycode = (event.keyCode ? event.keyCode : event.which);
    if(keycode == '13'){
        $(".btn-outline-primary").click();  
    }
    //Stop the event from propogation to other handlers
    event.stopPropagation();
  });


// Clear alert on timer 
function clearAlert() {
    $("#alert-user").empty()
}
   

// This will listen to click events and go back to the previous page
    $("#go-back").click(function (){
        window.history.back();
    });





// RESET button 
$("#danger-btn").click(function(){
    $("#loading-dlt").empty().html('<div class="spinner-border text-danger" \
    role="status"><span class="visually-hidden">Loading...</span></div>')
    /*
    let userId = $("input[type='hidden']").attr("data-user-id")
    let foodId = $("input[type='hidden']").attr("data-food-id")
    */
   console.log("complete DELETE method used")
    $.ajax({
        type: 'DELETE',
        url: "http://18.205.104.232:5001/api/v1/reviews/" + reviewId,
        headers: {
            'Content-Type': 'application/json'
        },
        data: JSON.stringify({
            user_id: userId,
        }),
        success: function(response){
            console.log(response)
            $(".this-usr-comment").text("")
            $("#edit").text("")
            $("#delete").text("")
            $(".star-val").text("")
            $(".fa-solid").mouseleave()
            $(".btn-outline-primary").prop("disabled", false)
            $("#alert-user").empty().html('<div class="alert alert-danger"\
             role="alert">Your entire review is RESETED !!!</div>')
             $("#loading-dlt").empty()
             $(".usr-comment").css("visibility", "hidden").css("height", "0").css("width", "0").css("padding", "0").css("margin", "0")
             const myTimeout = setTimeout(clearAlert, 3000);
             if ((reviewId != null) || (reviewId != "") || ($("input[type='hidden']") != null) || ($("input[type='hidden']") != "")) {
                reviewId = null;
                $("input[type='hidden']").attr("data-review-id", "")
             }
        },
        error: function(error){
            console.log(error);
            alert("You are not connected to the internet !", error)
            $("#loading-dlt").empty()
        }
    });
    
})



























    /**********************************JS FOR RATING****************************************** */
    
})