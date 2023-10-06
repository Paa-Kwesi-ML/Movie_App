function logins(){
    var userName=prompt("Input your username:");
    var password=prompt("Input your password:");
    if(userName==null){  
        alert ("Please enter your name well!");
        var userNameAgain=prompt("Please enter your name again");
        alert("better"+ " " + userNameAgain);
    }else
    {
        alert ("Welcome to the MCU"+" "+ userName);
    
}
}
function Sign_up(){
var data=document.forms["myForm"][("username")/*,("irstname")*/].value;
    if(data==""){
        alert("Please enter your details!");
        return false;
    }
    alert("Congratulations! You have signed up!"+" "+ data);
}

