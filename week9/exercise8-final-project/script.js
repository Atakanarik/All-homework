const todoInput = document.getElementById('todo-input');
const addBtn = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');
const clearAllBtn = document.getElementById('clear-all-btn');

// 1. Load tasks from Local Storage when the page opens
let tasks = JSON.parse(localStorage.getItem('myTasks')) || [];
renderTasks();

// 2. Function to render tasks to the UI
function renderTasks() {
    todoList.innerHTML = '';
    tasks.forEach((task, index) => {
        const li = document.createElement('li');
        li.innerHTML = `
            ${task}
            <button onclick="deleteTask(${index})">Delete</button>
        `;
        todoList.appendChild(li);
    });
}

// 3. Add a new task
addBtn.addEventListener('click', () => {
    const newTask = todoInput.value.trim();
    if (newTask) {
        tasks.push(newTask); // Add to array
        saveAndRefresh();    // Save to storage and update UI
        todoInput.value = '';
    }
});

// 4. Delete a specific task
function deleteTask(index) {
    tasks.splice(index, 1);
    saveAndRefresh();
}

// 5. Clear everything
clearAllBtn.addEventListener('click', () => {
    tasks = [];
    saveAndRefresh();
});

// 6. Helper function to save to Local Storage
function saveAndRefresh() {
    localStorage.setItem('myTasks', JSON.stringify(tasks));
    renderTasks();
}
