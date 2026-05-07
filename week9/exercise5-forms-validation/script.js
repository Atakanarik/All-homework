/**
 * Exercise 5: Forms & Validation
 * ================================
 */

const form = document.querySelector('#registration-form');
const submitBtn = document.querySelector('#submit-btn');

// ============================================================
// HELPER: Show or clear an error on a field
// ============================================================
function showError(inputId, message) {
    const input = document.getElementById(inputId);
    const errorSpan = document.getElementById(`error-${inputId}`);
    input.classList.add('invalid');
    input.classList.remove('valid');
    errorSpan.textContent = message;
}

function clearError(inputId) {
    const input = document.getElementById(inputId);
    const errorSpan = document.getElementById(`error-${inputId}`);
    input.classList.remove('invalid');
    input.classList.add('valid');
    errorSpan.textContent = "";
}

// ============================================================
// TASK 2: Individual Field Validators
// ============================================================

function validateUsername() {
    const input = document.getElementById('username');
    if (input.value.trim().length < 3) {
        showError('username', 'Username must be at least 3 characters.');
        return false;
    }
    clearError('username');
    return true;
}

function validateEmail() {
    const email = document.getElementById('email').value;
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!regex.test(email)) {
        showError('email', 'Please enter a valid email address.');
        return false;
    }
    clearError('email');
    return true;
}

function validatePassword() {
    const pass = document.getElementById('password').value;
    const hasDigit = /\d/.test(pass);
    
    updatePasswordStrength(pass); // Task 4

    if (pass.length < 8 || !hasDigit) {
        showError('password', 'Must be 8+ characters with at least one digit.');
        return false;
    }
    clearError('password');
    return true;
}

function validateConfirmPassword() {
    const pass = document.getElementById('password').value;
    const confirm = document.getElementById('confirm-password').value;
    if (confirm !== pass || confirm === "") {
        showError('confirm-password', 'Passwords do not match.');
        return false;
    }
    clearError('confirm-password');
    return true;
}

function validateBirthDate() {
    const dateVal = document.getElementById('birth-date').value;
    if (!dateVal) {
        showError('birth-date', 'Please select your birth date.');
        return false;
    }
    
    const birthDate = new Date(dateVal);
    const age = new Date().getFullYear() - birthDate.getFullYear();
    
    if (age < 18 || age > 120) {
        showError('birth-date', 'You must be between 18 and 120 years old.');
        return false;
    }
    clearError('birth-date');
    return true;
}

function validateCountry() {
    const country = document.getElementById('country').value;
    if (country === "") {
        showError('country', 'Please select a country.');
        return false;
    }
    clearError('country');
    return true;
}

function validateTerms() {
    const terms = document.getElementById('terms');
    if (!terms.checked) {
        showError('terms', 'You must agree to the terms.');
        return false;
    }
    clearError('terms');
    return true;
}

// ============================================================
// TASK 4: Password Strength Indicator
// ============================================================
function updatePasswordStrength(password) {
    const strengthEl = document.getElementById('password-strength');
    if (!strengthEl) return;

    let strength = "Weak";
    strengthEl.className = "strength-meter weak";

    if (password.length >= 8 && /\d/.test(password) && /[A-Z]/.test(password)) {
        strength = "Strong";
        strengthEl.className = "strength-meter strong";
    } else if (password.length >= 6) {
        strength = "Fair";
        strengthEl.className = "strength-meter fair";
    }
    
    strengthEl.textContent = `Strength: ${strength}`;
}

// ============================================================
// TASK 5: Bio Character Counter
// ============================================================
const bioTextarea = document.querySelector('#bio');
const charCount = document.querySelector('#char-count');

if (bioTextarea) {
    bioTextarea.addEventListener('input', () => {
        const length = bioTextarea.value.length;
        charCount.textContent = `${length} / 200 characters`;
        
        if (length > 200) {
            charCount.classList.add('over-limit');
            submitBtn.disabled = true;
        } else {
            charCount.classList.remove('over-limit');
            submitBtn.disabled = false;
        }
    });
}

// ============================================================
// TASK 2: Attach real-time listeners
// ============================================================
const fields = [
    { id: 'username', validator: validateUsername },
    { id: 'email', validator: validateEmail },
    { id: 'password', validator: validatePassword },
    { id: 'confirm-password', validator: validateConfirmPassword },
    { id: 'birth-date', validator: validateBirthDate },
    { id: 'country', validator: validateCountry },
    { id: 'terms', validator: validateTerms }
];

fields.forEach(field => {
    const element = document.getElementById(field.id);
    if (element) {
        // 'blur' triggers when the user leaves the input field
        element.addEventListener('blur', field.validator);
        // 'input' for real-time as they type
        if (field.id === 'password' || field.id === 'confirm-password') {
            element.addEventListener('input', field.validator);
        }
    }
});

// ============================================================
// TASK 3: Submit Handler
// ============================================================
form.addEventListener('submit', function(event) {
    event.preventDefault();

    // Run all validators
    const results = [
        validateUsername(),
        validateEmail(),
        validatePassword(),
        validateConfirmPassword(),
        validateBirthDate(),
        validateCountry(),
        validateTerms()
    ];

    const isFormValid = results.every(result => result === true);

    if (isFormValid) {
        document.getElementById('success-message').classList.remove('hidden');
        form.classList.add('hidden');
        console.log("Form Submitted Successfully!");
    } else {
        // Scroll to the first error
        const firstInvalid = document.querySelector('.invalid');
        if (firstInvalid) {
            firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
            firstInvalid.focus();
        }
    }
});
