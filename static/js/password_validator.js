$(document).ready(function () {

    function checkPassword(){
        let password = $("#user_password").val();
        let retype = $("#retype").val();
        if (password != retype) {
            $("#retype").addClass("password-incorrect");
            $("#login-button").addClass("disabled");
        }
        else if (password == retype) {
            $("#retype").removeClass("password-incorrect");
            $("#retype").addClass("password-correct");
            $("#login-button").removeClass("disabled");
        }
    }

    $("#user_password").keyup(checkPassword);
    $("#retype").keyup(checkPassword);
    
});