document.addEventListener('DOMContentLoaded', function() {

    // --- Navbar Scroll Effect ---
    const navbar = document.querySelector('.navbar-custom');
    if (navbar) {
        // Add scrolled class on page load if already scrolled
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        }
        // Add scroll listener
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('navbar-scrolled');
            } else {
                navbar.classList.remove('navbar-scrolled');
            }
        });
    }

    // --- Student Dashboard AI Analysis Simulation ---
    const analyzeBtn = document.getElementById('analyzeBtn');
    const resumeFile = document.getElementById('resumeFile');
    const spinner = document.getElementById('analysis-spinner');
    const resultsDiv = document.getElementById('analysis-results');
    const uploadPrompt = document.getElementById('upload-prompt');

    if (analyzeBtn) {
        analyzeBtn.addEventListener('click', function() {
            if (resumeFile.files.length === 0) {
                // Using a Bootstrap 5 modal for alerts would be even better
                alert('Please select a resume file first.');
                return;
            }

            if(resultsDiv) resultsDiv.style.display = 'none';
            if(uploadPrompt) uploadPrompt.style.display = 'none';
            if(spinner) spinner.style.display = 'flex'; // Use flex for centering
            
            // Simulate AI processing
            setTimeout(() => {
                if(spinner) spinner.style.display = 'none';
                if(resultsDiv) {
                    resultsDiv.style.display = 'block';
                    // Add a fade-in effect
                    resultsDiv.classList.add('fade-in');
                }
            }, 2500); // 2.5-second delay
        });
    }

    // --- Form Submission Simulation Modal ---
    const jobApplyForm = document.getElementById('jobApplyForm');
    if(jobApplyForm) {
        jobApplyForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent actual submission for demo
            
            const successModal = new bootstrap.Modal(document.getElementById('applicationSuccessModal'));
            successModal.show();
        });
    }
});

// Add a simple fade-in animation class to CSS if you want
const style = document.createElement('style');
style.innerHTML = `
  .fade-in {
    animation: fadeInAnimation 0.5s ease-in forwards;
  }
  @keyframes fadeInAnimation {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
`;
document.head.appendChild(style);
