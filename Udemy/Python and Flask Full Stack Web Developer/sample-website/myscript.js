var newImage = document.querySelector('img');

newImage.onclick = function (){
    var myImages = newImage.getAttribute('src');

    if (myImages === "./images/prof_face.jpeg"){
        newImage.setAttribute("src", "./images/Mrutyunjay.jpeg");
    } else {
        newImage.setAttribute("src", "./images/prof_face.jpeg")
    }

}

// personalized welcome message 
var nameButton = document.querySelector("button");
var myHeading = document.querySelector("h1");

function setUserName() {
    "use strict";
    var myName = window.prompt("Please enter your Name.");
    localStorage.setItem("name", myName);
    myHeading.textContent = "Have a nice Day, " + myName;
}

if (!localStorage.getItem("name")) {
    setUserName();
} else {
    var storedName = localStorage.getItem("name");
    myHeading.textContent = "Have a nice Day, " + storedName;
}

nameButton.onclick = function() {
    "use strict";
    setUserName();
}
