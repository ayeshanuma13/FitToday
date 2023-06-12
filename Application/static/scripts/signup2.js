document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();

    if(document.signup.username.value==""){
        document.getElementById("result").innerHTML="Enter Username";
        return false;
    }

    else if(document.signup.username.value.length<6){
        document.getElementById("result").innerHTML="Username must have at least 6 characters";
        return false;
    }

    else if(document.signup.email.value==""){
        document.getElementById("result").innerHTML="Enter Email";
        return false;
    }

    else if(document.signup.password.value==""){
        document.getElementById("result").innerHTML="Enter Password";
        return false;
    }

    else if(document.signup.password.value.length<8){
        document.getElementById("result").innerHTML="Password must have at least 8 characters";
        return false;
    }

    else if(document.signup.cpassword.value==""){
        document.getElementById("result").innerHTML="Enter Confirmed Password";
        return false;
    }

    else if(document.signup.password.value!=document.signup.cpassword.value){
        document.getElementById("result").innerHTML="Passwords don't match";
        return false;
    }

    else if(document.signup.password.value==document.signup.cpassword.value){
        popup.classList.add("open-slide")
        return false;
    }
    event.target.submit();
});