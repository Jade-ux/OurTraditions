  $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.tooltipped').tooltip();
     $('select').formSelect();
  });

//Country autocomplete for the add-tradition page
$(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "Afganistan": null,
        "Albania": null,
        "Algeria": null,
      },
    });
  });