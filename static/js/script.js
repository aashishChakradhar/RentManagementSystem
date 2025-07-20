document.addEventListener("DOMContentLoaded", function () {
    // Close error messages
    document.querySelectorAll(".close-error").forEach(function (btn) {
        btn.addEventListener("click", function () {
            this.parentElement.style.display = "none";
        });
    });

    // Greeting message
    var hour = new Date().getHours();
    var user = document.getElementById("greeting")?.dataset.username || "User";
    var greet = (hour >= 0 && hour < 12)
        ? "Good Morning"
        : (hour <= 16)
        ? "Good Afternoon"
        : "Good Evening";
    
    var greetingElement = document.getElementById("greeting-message");
    if (greetingElement) {
        greetingElement.textContent = `${greet}, ${user}!!`;
    }

    // Date section
    var today = new Date().toISOString().split("T")[0];
    var todayDateElem = document.getElementById("todayDate");
    if (todayDateElem) {
        todayDateElem.textContent = today;
    }

    var inputDate = document.getElementById("date");
    if (inputDate) {
        inputDate.value = today;
    }

    // Building select toggle
    var actionDropdown = document.getElementById("action");
    if (actionDropdown) {
        actionDropdown.addEventListener("change", function () {
            var action = this.value;
            var buildingSelectContainer = document.getElementById("building-select-container");
            if (buildingSelectContainer) {
                buildingSelectContainer.style.display =
                    action === "update" || action === "delete" ? "block" : "none";
            }
        });
    }
});
