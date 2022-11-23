$(document).ready(function() {
    let previouState = $(".restaurants").html()
    let input = document.querySelector("input")
    input.addEventListener("input", async function(){
        console.log(input.value, (input.value).length)
        if ((input.value).length == 0) {
            document.querySelector(".restaurants").innerHTML = previouState
        } else {
            $(".restaurants").empty()
            let response =  await fetch('/search?q=' + input.value)
            .catch(error => {
                alert(`You are not connected to the internet ! ${error}`)
            })
            let restaurantLists = await response.json()
            let html = ''
            for (let i = 0; i < restaurantLists.length; i++) {
                let restaurant = '<section class="restaurant">\
                <h2>' + restaurantLists[i].name + 'Kitfo bet &nbsp\
                 &nbsp <i class="fa-solid fa-utensils"></i></h2>\
                 <div class="restr-descr"><article><p class="description"></p>\
                 ' + restaurantLists[i].description + '</p></article>\
                 <div><img class="img-restr" src="' + restaurantLists[i].image + '"\
                   alt="Restaurant Image"></div></div><div class="hr-line"></div>\
                   </section>'
                html += restaurant
            }
            document.querySelector(".restaurants").innerHTML = html
        }
    })

    let myVar = setInterval(myTimer ,1000);
    function myTimer() {
    const d = new Date();
    document.getElementById("time").innerHTML = d.toLocaleTimeString();
}
})