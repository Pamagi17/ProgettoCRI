function confirmationBanner() {
    $("#banner-container").slideDown(function () {
        // Showing the banner
    });
    setTimeout(function () {
        $("#banner-container").slideUp("slow", function () {
            // Hiding the banner
        });
    }, 5000);
};

$(document).ready(function () {
    confirmationBanner()
});