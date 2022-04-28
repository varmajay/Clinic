/*=========================================================================================
    File Name: coming-soon.js
    Description: Coming Soon
==========================================================================================*/

/*******************************
 *       js of Countdown        *
 ********************************/

$(document).ready(function () {

  var todayDate = new Date();
  var dd = todayDate.getDate();
  var mm = todayDate.getMonth() + 1;
  var yy = todayDate.getFullYear();
  var currentDate = yy + "/" + (mm + 2) + "/" + dd;

  $('#clockFlat').countdown(currentDate).on('update.countdown', function (event) {
    var $this = $(this).html(event.strftime('' +
      '<div class="clockCard px-3 py-3 mr-3 mb-3 d-inline-block"> <span class="text-dark">%D</span> <br> <p class="lead mt-2 mb-0 text-dark">Day%!D </p> </div>' +
      '<div class="clockCard px-3 py-3 mr-3 mb-3 d-inline-block"> <span class="text-dark">%H</span> <br> <p class="lead mt-2 mb-0 text-dark">Hour%!H </p> </div>' +
      '<div class="clockCard px-3 py-3 mr-3 mb-3 d-inline-block"> <span class="text-dark">%M</span> <br> <p class="lead mt-2 mb-0 text-dark">Minute%!M </p> </div>' +
      '<div class="clockCard px-2 py-3 mr-3 mb-3 d-inline-block"> <span class="text-dark">%S</span> <br> <p class="lead mt-2 mb-0 text-dark">Second%!S </h5> </div>'
    ))
  });
});
