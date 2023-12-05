// Script that toggles between red and green
// when user click on ID w/ toggle_header
$(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
