// Fetches from URL and displays 'hello' from said fetch in HTML tag
$(function () {
  // AJAX request fer data
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (data) {
      // Updating translated content
      $('#hello').text(data.hello);
    },
    error: function (error) {
      console.error('Error', error);
    }
  });
});
