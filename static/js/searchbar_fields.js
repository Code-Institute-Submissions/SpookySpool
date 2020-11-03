$(document).ready(function () {  
    $("#show_options").click(function () {

        if ($("#form_options").is(':visible')) {
           $("#show_options>i").removeClass('fa-angle-up').addClass('fa-angle-down');
           $("#form_options").slideUp(250);
        } else {
           $("#show_options>i").removeClass('fa-angle-down').addClass('fa-angle-up');
           $("#form_options").slideDown(250);
        }
    });
  });
