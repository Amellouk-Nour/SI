document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    clearErrors();

    let valid = true;

    if (username.length < 4) {
        showError('usernameError', 'Username must be at least 4 characters');
        valid = false;
    }

    if (password.length < 6) {
        showError('passwordError', 'Password must be at least 6 characters');
        valid = false;
    }

    if (valid) {
        // Process the form submission (e.g., send to server)
        alert('Form submitted successfully!');
    }
});

function showError(elementId, message) {
    document.getElementById(elementId).textContent = message;
}

function clearErrors() {
    document.querySelectorAll('.error-message').forEach(element => {
        element.textContent = '';
    });
}
