/**
 * Exercise 4: JavaScript & the DOM
 * ==================================
 */

// ============================================================
// TASK 1 — Console Warmup
// ============================================================

// TODO 1a: Select the element with id "main-title" and change text
const title = document.getElementById('main-title');
title.textContent = "DOM Mastery 🚀";

// TODO 1b: Select ALL elements with class "card", log how many there are
const cards = document.querySelectorAll('.card');
console.log(`Total cards found: ${cards.length}`);

// TODO 1c: Select the element with id "target-box" and change color
const targetBox = document.getElementById('target-box');
targetBox.style.backgroundColor = "#2ecc71"; // Nice green


// ============================================================
// TASK 2 — Click Counter
// ============================================================

const countDisplay = document.querySelector('#count-display');
const btnDec = document.querySelector('#btn-decrement');
const btnRes = document.querySelector('#btn-reset');
const btnInc = document.querySelector('#btn-increment');

let count = 0;

function updateCountDisplay() {
    countDisplay.textContent = count;
    
    // Manage classes for styling
    if (count === 0) {
        countDisplay.classList.add('zero');
        countDisplay.classList.remove('high');
    } else if (count > 5) {
        countDisplay.classList.add('high');
        countDisplay.classList.remove('zero');
    } else {
        countDisplay.classList.remove('zero', 'high');
    }
}

btnInc.addEventListener('click', () => {
    count++;
    updateCountDisplay();
});

btnDec.addEventListener('click', () => {
    if (count > 0) { // Don't go below 0
        count--;
        updateCountDisplay();
    }
});

btnRes.addEventListener('click', () => {
    count = 0;
    updateCountDisplay();
});

updateCountDisplay();


// ============================================================
// TASK 3 — Dynamic List Builder
// ============================================================

const listInput = document.querySelector('#list-input');
const btnAdd = document.querySelector('#btn-add-item');
const dynamicList = document.querySelector('#dynamic-list');

btnAdd.addEventListener('click', () => {
    const text = listInput.value.trim();
    
    if (text === "") {
        alert("Please type something before adding!");
        return;
    }

    // Create <li> and <span> for text to keep it separate from button
    const li = document.createElement('li');
    li.innerHTML = `${text} <button class="delete-btn">×</button>`;
    
    dynamicList.appendChild(li);
    listInput.value = "";
    listInput.focus();
});

// Event Delegation for delete buttons
dynamicList.addEventListener('click', function(event) {
    if (event.target.classList.contains('delete-btn')) {
        event.target.parentElement.remove();
    }
});


// ============================================================
// TASK 4 — Show / Hide Toggle
// ============================================================

const toggleBtn = document.querySelector('#btn-toggle');
const detailsDiv = document.querySelector('.details');

toggleBtn.addEventListener('click', () => {
    const isHidden = detailsDiv.classList.toggle('hidden');
    toggleBtn.textContent = isHidden ? "Show Details" : "Hide Details";
});


// ============================================================
// TASK 5 — Color Mixer
// ============================================================

const sliderR = document.querySelector('#slider-r');
const sliderG = document.querySelector('#slider-g');
const sliderB = document.querySelector('#slider-b');
const valR = document.querySelector('#val-r');
const valG = document.querySelector('#val-g');
const valB = document.querySelector('#val-b');
const colorPreview = document.querySelector('#color-preview');
const hexDisplay = document.querySelector('#hex-display');

function updateColor() {
    const r = parseInt(sliderR.value);
    const g = parseInt(sliderG.value);
    const b = parseInt(sliderB.value);

    // Update text spans
    valR.textContent = r;
    valG.textContent = g;
    valB.textContent = b;

    // Set background
    const rgbColor = `rgb(${r}, ${g}, ${b})`;
    colorPreview.style.backgroundColor = rgbColor;

    // Convert to Hex
    const rHex = r.toString(16).padStart(2, '0');
    const gHex = g.toString(16).padStart(2, '0');
    const bHex = b.toString(16).padStart(2, '0');
    
    hexDisplay.textContent = `#${rHex}${gHex}${bHex}`.toUpperCase();
}

// Add input listeners
[sliderR, sliderG, sliderB].forEach(slider => {
    slider.addEventListener('input', updateColor);
});

updateColor();
