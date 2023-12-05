// Script that adds a <li> element to a
// list when the user clicks on the tag
$(function () {
  $('#add_item').click(function () {
    var newItem = $('<li>Item</li>');
    // Append new tag to <ul> w/ specified class
    $('ul.my_list').append(newItem);
  });
});
