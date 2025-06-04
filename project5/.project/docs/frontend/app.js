// app.js

// Wait for the document to be fully loaded before running any logic
// Fetches all tasks and sets up the form event listener
document.addEventListener('DOMContentLoaded', () => {
    fetchTasks();
    const addTaskForm = document.getElementById('add-task-form');
    if (addTaskForm) {
        addTaskForm.addEventListener('submit', handleAddTask);
    }
});

// Fetches the list of tasks from the backend API and displays them
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

// Display all tasks in the unordered list element with a delete button for each
default export function displayTasks(tasks) {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        // Show title, and if the task is done
        li.textContent = task.title + (task.done ? ' (done)' : '');
        if (task.due_date) {
            li.textContent += ` - Due: ${task.due_date}`;
        }
        // Create and append a delete button
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.className = 'delete-btn';
        deleteBtn.addEventListener('click', () => handleDeleteTask(task.id));
        li.appendChild(deleteBtn);

        taskList.appendChild(li);
    });
}

// Handle form submission for adding a new task
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

    // Prepare the task object to send
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
            // Clear the form inputs
            titleInput.value = '';
            dueDateInput.value = '';
            fetchTasks(); // Refresh task list
        })
        .catch(error => {
            alert('Failed to add task.');
        });
}

// Delete a task by its ID, and refresh the list upon success
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
