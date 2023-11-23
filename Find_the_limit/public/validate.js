function validateLogin() {
    const username = document.getElementById('username').value;
    const pin = parseInt(document.getElementById('pin').value);

    // Check if PIN = PIN + 1 due to Number.MAX_SAFE_INTEGER in JS
    if (pin === pin + 1) {
        // Load the flag page and print the flag
        window.location.href = '/flag?pin=' + pin;
    } else {
        alert('Incorrect PIN. Try again!');
    }
}
