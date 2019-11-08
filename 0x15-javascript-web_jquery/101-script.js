$(document).ready(function () {
    const item = "<li>Item</li>";

    $('#add_item').click(function () {
      $('.my_list').append(item);
    });

    $('#remove_item').click(function () {
      $('li:last').remove();
    });

    $('#clear_list').click(function () {
      $('ul').empty();
    });
  });
