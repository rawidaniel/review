$(document).ready(function () {
  let previouState = $('.restaurants').html();
  let input = document.querySelector('input');
  input.addEventListener('input', async function () {
    let searchStr = input.value;
    let serachRegex = new RegExp(searchStr, 'i');
    console.log(searchStr, searchStr.length);

    $('#ser-loading')
      .empty()
      .html(
        '<div class="spinner-grow text-light" role="status">\
        <span class="visually-hidden">Loading...</span></div>'
      );

    if (searchStr.length == 0) {
      document.querySelector('.restaurants').innerHTML = previouState;
      $('#ser-loading').empty();
    } else {
      $('.restaurants').empty();
      let response = await fetch(
        'http://18.205.104.232:5001/api/v1/restaurants'
      ).catch((error) => {
        alert(`You are not connected to the internet ! ${error}`);
      });
      let restaurantLists = await response.json();
      let html = '';
      for (let i = 0; i < restaurantLists.length; i++) {
        if (serachRegex.test(restaurantLists[i].name)) {
          var restaurant =
            '<a href="/foods?restaurant_id=' +
            restaurantLists[i].id +
            '"><section class="restaurant"><h2>' +
            restaurantLists[i].name +
            '&nbsp\
                    &nbsp <i class="fa-solid fa-utensils"></i></h2>\
                    <div class="restr-descr"><article><p class="description"></p>\
                    ' +
            restaurantLists[i].description +
            '</p></article>\
                    <div><img class="img-restr" src="./static/images/uploads/' +
            restaurantLists[i].image +
            '"\
                      alt="Restaurant Image"></div></div><div class="hr-line"></div>\
                      </section></a>';
          html += restaurant;
        }
      }

      if (html == '') {
        document.querySelector(
          '.restaurants'
        ).innerHTML = `<h1 style="color: red">No results found for "${searchStr}"</h1>`;
      } else {
        document.querySelector('.restaurants').innerHTML = html;
      }
      $('#ser-loading').empty();
    }
  });

  /*
    let myVar = setInterval(myTimer ,1000);
    function myTimer() {
    const d = new Date();
    document.getElementById("time").innerHTML = d.toLocaleTimeString();
    
    }
    */
});
