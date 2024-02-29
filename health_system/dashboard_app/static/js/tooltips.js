document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("#successPosts");
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission behavior
        const formData = new FormData(form);
        fetch(form.action, {
            method: form.method,
            body: formData,
        })
            .then(response => {
                if (response.ok) {
                    showTooltip();
                } else {
                    console.error("Form submission failed");
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
    });
});

function showTooltip() {
    const tooltip = document.querySelector("#tooltip");
    tooltip.style.display = "block";
    setTimeout(function () {
        tooltip.style.display = "none";
    }, 5000); // Hide the tooltip after 3 seconds (adjust as needed)
}
