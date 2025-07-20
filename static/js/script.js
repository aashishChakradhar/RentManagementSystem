document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".close-error").forEach(function (btn) {
        btn.addEventListener("click", function () {
        this.parentElement.style.display = "none";
        });
    });
});

var hour = new Date().getHours();
var user = document.getElementById("greeting").dataset.username;
var greet = (hour>=0 && hour<12)?"Good Morning":(hour<=16)?"Good Afternoon":"Good Evening";
document.getElementById("greeting-message").textContent = `${greet}, ${user}!!`;


var today =  new Date().toISOString().substr(0, 10); 

document.getElementById("todayDate").textContent = today;
document.getElementById("date").value = today;

