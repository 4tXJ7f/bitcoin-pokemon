function make_button_fn(button) {
  $('#press-' + button).on('click', function(e) {
    $.get("/press/" + button);
  });
}

$(document).ready(function () {
  var buttons = ['left', 'up', 'down', 'right', 'a', 'b', 'start', 'select'];
  for (var i = 0; i < buttons.length; i++) {
    make_button_fn(buttons[i]);
  }
});
