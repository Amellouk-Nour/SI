<script>
document.addEventListener("DOMContentLoaded", function() {

    // Get the form element
    var form = document.querySelector('form');

    // Function to validate form fields
    function validateForm() {
        var isValid = true;
        // Here you can add more validation logic for each field
        form.querySelectorAll('input[required], select[required]').forEach(function(input) {
            if (!input.value) {
                console.error(input.name + ' is required');
                isValid = false;
            }
        });

        return isValid;
    }

    // Function to handle form submission
    function handleFormSubmit(event) {
        event.preventDefault();

        // Check if form is valid
        if (!validateForm()) {
            alert('Please fill in all the required fields.');
            return;
        }

        // If form is valid, you can send the data to server here
        // For demonstration, we'll just log it to the console
        var formData = new FormData(form);
        var formProps = Object.fromEntries(formData);
        console.log(formProps);

        // To send the form data to the server using fetch:
        // fetch('/your-endpoint', {
        //     method: 'POST',
        //     body: formData
        // })
        // .then(response => response.json())
        // .then(data => console.log(data))
        // .catch(error => console.error('Error:', error));
    }

    // Attach the submission handler to form's 'submit' event
    form.addEventListener('submit', handleFormSubmit);
});
</script>
