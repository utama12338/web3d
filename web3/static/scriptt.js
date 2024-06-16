// script.js

document.addEventListener('DOMContentLoaded', () => {
    const userForm = document.getElementById('user-form');
    const userTableBody = document.querySelector('.user-table tbody');

    // Handle form submission to add a new user
    userForm.addEventListener('submit', (event) => {
        event.preventDefault();
        
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const role = document.getElementById('role').value;
        
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td>${username}</td>
            <td>${email}</td>
            <td>${role}</td>
        `;
        
        userTableBody.appendChild(newRow);

        // Clear the form inputs
        userForm.reset();

        // Add click event to the new row
        newRow.addEventListener('click', () => {
            highlightRow(newRow);
        });
    });

    // Function to highlight a row
    function highlightRow(row) {
        // Remove highlight from any previously highlighted row
        const highlightedRow = document.querySelector('.highlight');
        if (highlightedRow) {
            highlightedRow.classList.remove('highlight');
        }
        // Add highlight to the clicked row
        row.classList.add('highlight');
    }

    // Add click event to existing rows
    const rows = userTableBody.querySelectorAll('tr');
    rows.forEach(row => {
        row.addEventListener('click', () => {
            highlightRow(row);
        });
    });
});
