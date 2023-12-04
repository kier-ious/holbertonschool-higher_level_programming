//  Adds the class 'red' to <header> tag when user clicks specified tag
$(function () {
  $('#red_header').click(function () {
    // Adding 'red' class to <header>
    $('header').addClass('red');
  });
});
