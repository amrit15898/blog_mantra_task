
document.addEventListener("DOMContentLoaded", function() {
    const showEmailFormButton = document.getElementById("showEmailForm");
    const emailForm = document.querySelector(".email-form");

    showEmailFormButton.addEventListener("click", function() {
        emailForm.style.display = "block";
        showEmailFormButton.style.display = "none";
    });
});