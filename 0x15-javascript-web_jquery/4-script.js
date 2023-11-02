#!/usr/bin/node

$(document).ready(function () {
  $("#toggle_header").on("click", function () {
    $("header").toggleClass("red green");
  });
});
