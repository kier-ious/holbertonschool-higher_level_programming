// Update text color when user clicks on <header>
$(function () {
  $('#red_header').click(function () {
    // Select <header> element using jQuery
    $('header').css('color', '#FF0000');
  });
});
