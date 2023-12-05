// Script that fetches and lists all movie titles from URL
$(function () {
  // AJAX request fer data
  $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      // Select specific tag element
      const listElement = $('#list_movies');

      // Iterates through movie data then appends to list
      data.results.forEach(function (movie) {
        listElement.append('<li>' + movie.title + '</li>');
      });
    },
    error: function (error) {
      console.error('Error', error);
    }
  });
});
