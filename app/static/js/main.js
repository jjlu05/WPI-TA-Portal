document.addEventListener("DOMContentLoaded", function () {
    /**
     * Initializes a progress bar to track form field completion.
     * @param {string} formId - The ID of the form element.
     * @param {string} progressBarId - The ID of the progress bar element.
     */
    function initializeProgressBar(formId, progressBarId) {
        const form = document.getElementById(formId);
        const progressBar = document.getElementById(progressBarId);

        if (!form || !progressBar) {
            console.warn("Progress bar setup: Missing form or progress bar element.");
            return;
        }

        const fields = form.querySelectorAll('input, select, textarea');

        function updateProgress() {
            let filled = 0;
            fields.forEach(field => {
                if (field.value.trim() !== '') {
                    filled++;
                }
            });
            const progress = Math.round((filled / fields.length) * 100);
            progressBar.style.width = progress + '%';
            progressBar.setAttribute('aria-valuenow', progress);
            progressBar.textContent = progress + '%';
        }

        // Attach event listeners to each field
        fields.forEach(field => {
            field.addEventListener('input', updateProgress);
        });

        // Initialize the progress bar
        updateProgress();
    }

    // Example: Initialize the progress bar for a specific form
    initializeProgressBar('student-form', 'progress-bar');
});
