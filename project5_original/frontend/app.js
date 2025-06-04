// app.js

document.addEventListener('DOMContentLoaded', () => {
    fetchTasks();
    const addTaskForm = document.getElementById('add-task-form');
    if (addTaskForm) {
        addTaskForm.addEventListener('submit', handleAddTask);
    }
});

function fetchTasks() {
    fetch('http://localhost:8000/tasks')
        .then(response => response.json())
        .then(data => {
            displayTasks(data);
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
        });
}

function displayTasks(tasks) {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.title + (task.done ? ' (done)' : '');
        if (task.due_date) {
            li.textContent += ` - Due: ${task.due_date}`;
        }
        // Create delete button
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.className = 'delete-btn';
        deleteBtn.addEventListener('click', () => handleDeleteTask(task.id));
        li.appendChild(deleteBtn);

        taskList.appendChild(li);
    });
}

function handleAddTask(event) {
    event.preventDefault();
    const titleInput = document.getElementById('task-title');
    const dueDateInput = document.getElementById('task-due-date');
    const title = titleInput.value.trim();
    const due_date = dueDateInput.value;

    if (!title) {
        alert('Task title is required');
        return;
    }

    const newTask = { title };
    if (due_date) {
        newTask.due_date = due_date;
    }

    fetch('http://localhost:8000/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newTask),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to add task');
            }
            return response.json();
        })
        .then(addedTask => {
            titleInput.value = '';
            dueDateInput.value = '';
            fetchTasks(); // Refresh task list
        })
        .catch(error => {
            alert('Failed to add task.');
        });
}

function handleDeleteTask(taskId) {
    fetch(`http://localhost:8000/tasks/${taskId}`, {
        method: 'DELETE',
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to delete task');
            }
            fetchTasks(); // Re-fetch tasks and update UI
        })
        .catch(error => {
            alert('Failed to delete task.');
        });
}
