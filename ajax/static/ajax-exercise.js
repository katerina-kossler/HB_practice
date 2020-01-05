"use strict";


// PART 1: SHOW A FORTUNE

function showFortune(evt) {
    // get the random fortune from '/fortune'
    // and show it in the #fortune-text div
  $.get('/fortune', (res) => {
    $('#fortune-text').html(res);
  });
}

$('#get-fortune-button').on('click', showFortune);



// PART 2: SHOW WEATHER

function showWeather(evt) {
    evt.preventDefault();

    let url = "/weather.json";
    let formData = {"zipcode": $("#zipcode-field").val()};


    // TODO: request weather with that URL and show the forecast in #weather-info
    $.get(url,formData,(res)=>{
      $("#weather-info").html(res.forecast);
    });
}

$("#weather-form").on('submit', showWeather);


// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    const melons = {
      'qty': $('#qty-field').val(),
      'melon_type': $('#melon-type-field').val()
    };

    $.post('/order-melons.json', melons, (res) => {
      $('#order-status').html(res.msg)
    });
    // TODO: show the result message after your form
    // TODO: if the result code is ERROR, make it show up in red (see our CSS!)
}

$("#order-form").on('submit', orderMelons);


