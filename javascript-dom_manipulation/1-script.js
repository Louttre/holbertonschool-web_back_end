document.getElementById('red_header').onclick = changeColor; 
var currentColor = "red";
function changeColor() { 
        if(currentColor == "red") { 
           document.body.style.color = "green";
           currentColor = "green";
        } else {
           document.body.style.color = "red";
           currentColor = "red";
        } 
    }
