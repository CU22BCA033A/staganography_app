// static/js/script.js

// Function to validate the encode form
function validateEncodeForm() {
    const imageInput = document.getElementById('image');
    const messageInput = document.getElementById('message');
    const secretKeyInput = document.getElementById('secret_key');

    if (!imageInput.files || imageInput.files.length === 0) {
        alert('Please upload an image.');
        return false;
    }

    if (messageInput.value.trim() === '') {
        alert('Please enter a message to hide.');
        return false;
    }

    if (secretKeyInput.value.trim() === '') {
        alert('Please enter a secret key.');
        return false;
    }

    return true;
}

// Function to validate the decode form
function validateDecodeForm() {
    const imageInput = document.getElementById('image');
    const secretKeyInput = document.getElementById('secret_key');

    if (!imageInput.files || imageInput.files.length === 0) {
        alert('Please upload an image.');
        return false;
    }

    if (secretKeyInput.value.trim() === '') {
        alert('Please enter a secret key.');
        return false;
    }

    return true;
}

// Add event listeners to forms
document.addEventListener('DOMContentLoaded', function () {
    const encodeForm = document.querySelector('form[action="{{ url_for('encode') }}"]');
    const decodeForm = document.querySelector('form[action="{{ url_for('decode') }}"]');

    if (encodeForm) {
        encodeForm.addEventListener('submit', function (event) {
            if (!validateEncodeForm()) {
                event.preventDefault(); // Prevent form submission if validation fails
            }
        });
    }

    if (decodeForm) {
        decodeForm.addEventListener('submit', function (event) {
            if (!validateDecodeForm()) {
                event.preventDefault(); // Prevent form submission if validation fails
            }
        });
    }
});