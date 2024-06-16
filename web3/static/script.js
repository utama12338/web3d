// script.js

// Example: Add validation or other functionality
document.querySelector('form').addEventListener('submit', function(event) {
    // Example: Prevent form submission if inputs are invalid
    var username = document.getElementById('username').value.trim();
    var password = document.getElementById('password').value.trim();

    if (username === '' || password === '') {
        event.preventDefault(); // Prevent form submission
        alert('Please fill in all fields.');
    }
});
