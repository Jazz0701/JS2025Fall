$(document).ready(function(){
    $("#loginForm").on("submit", function(event)){
        event.preventDefault();

        let $username = $("username").val();
        let $email = $("$email").val();
        let $password = $("$password").val();
        
        console.log($email, $password, $username);

        // initialize a flag to check if the form is valid 
        let $isValid =true;

        if($username === ""){
            $("#usernameError").text("Username cannot be empty")
            $("#usernameError").css("color", "red")
            $isValid =false;
        }else{
            $("#usernameError").text("")
        }

        //if the password length id less than 8
        
        if($password === ""){
            $("#passwordError").text("Password cannot be empty")
            $("#passwordError").css("color", "red")
         isValid = false;
        }else if ($password.length < 8) {
            $("#passwordError").text("Password must be at least 8 characters").css("color", "red");
        isValid = false;
        }
        else{
            $("passwordError").text("")
        }

    })

      //email pattern
      let $emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/

      $emailPattern.test($email)

      if(!$emailPattern.test($email)){
        $("#emailError").ttext("Invlid email format")
      } else{
        $("#emailError").empty()

        if{ isValid){
            alert("Form submitted successfully")
            $("username").val("")
        }
        })

      })



