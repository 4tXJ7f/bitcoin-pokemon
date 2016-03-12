$('#press-left').on('click', function(e) {
  $.get("/press/left")
});

$('#press-right').on('click', function(e) {
  $.get("/press/right")
});
