  $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

  $('#password, #confirm-password').on('keyup', function(){
        if ($(this).val() == $('#password').val()){
          $('#password-message').html('Password is a match').css('color', 'green');
        }else
            $('#password-message').html('Password is not a match').css('color', 'red');
  });