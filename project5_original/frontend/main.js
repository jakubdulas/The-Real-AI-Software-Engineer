const API_URL = 'http://localhost:8001/tasks'; // Adjust port if your backend runs elsewhere

document.addEventListener('DOMContentLoaded', () => {
    fetchTasks();

    const form = document.getElementById('add-task-form');
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        const input = document.getElementById('task-title');
        const title = input.value.trim();
        if (title) {
            addTask(title);
            input.value = '';
        }
    });
});

function fetchTasks() {
    fetch(API_URL)
        .then(res => res.json())
        .then(tasks => {
            renderTasks(tasks);
        })
        .catch(err => {
            console.error('Failed to fetch tasks:', err);
        });
}

function addTask(title) {
    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: title })
    })
        .then(response => {
            if (!response.ok) throw new Error('Failed to add task');
            return response.json();
        })
        .then(() => {
            fetchTasks();
        })
        .catch(err => {
            alert('Error adding task: ' + err.message);
        });
}

function renderTasks(tasks) {
    const list = document.getElementById('task-list');
    list.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.title;
        li.className = task.status ? 'done' : '';
        // The delete button will be added/handled elsewhere
        list.appendChild(li);
    });
}
