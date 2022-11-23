$(document).ready(() => {


// Get rate and review from backend and put it on user page
    fetch('/api/review')
   .then(response => response.json())
   .then(data => {
      let infoData = JSON.stringify(data)
      let dataObject = JSON.parse(infoData)
      let starSet = dataObject.rate
      let textSet = dataObject.review
      
      if (starSet != 0) {
        $(".star-val").text(starSet)
        $(".fa-solid").mouseleave()
      }

      if (textSet != "") {
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
   })
   .catch(error => {
    alert(`You are not connected to the internet ! ${error}`)
    alert(`Failed to load your data! `)
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
        let userId = $("input[type='hidden']").attr("data-user-id")
        let foodId = $("input[type='hidden']").attr("data-food-id")
        $.ajax({
            type: 'POST',
            url: "/api/review",
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({
                review_text: textVal,
                user_id: userId,
                food_id: foodId
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
        let userId = $("input[type='hidden']").attr("data-user-id")
        let foodId = $("input[type='hidden']").attr("data-food-id")
        $.ajax({
            type: 'DELETE',
            url: "/api/review",
            headers: {
                'Content-Type': 'application/json'
            },
            data: JSON.stringify({
                user_id: userId,
                food_id: foodId
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
        console.log(starValEach, i)
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
})