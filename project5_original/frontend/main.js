// main.js
// Frontend logic for TODO App: fetch, display, add, and delete tasks using backend API

const API_BASE_URL = "http://127.0.0.1:8000"; // Adjust if needed

/**
 * Fetches all TODO tasks from the API.
 * @returns {Promise<Array>} Promise resolving to an array of task objects.
 */
async function getAllTasks() {
  const response = await fetch(`${API_BASE_URL}/tasks`);
  if (!response.ok) {
    throw new Error("Failed to fetch tasks");
  }
  return response.json();
}

/**
 * POST a new TODO task to the backend API.
 * @param {{title: string, due_date?: string}} task - Task object (title required, due_date optional).
 * @returns {Promise<Object>} Promise resolving to created task object from backend.
 */
async function createTask(task) {
  const response = await fetch(`${API_BASE_URL}/tasks`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(task),
  });
  if (!response.ok) {
    throw new Error("Failed to create new task");
  }
  return response.json();
}

/**
 * DELETE a TODO task from the backend API.
 * @param {number|string} id - ID of the task to delete.
 * @returns {Promise<void>} Resolves when deletion is successful.
 */
async function deleteTask(id) {
  const response = await fetch(`${API_BASE_URL}/tasks/${id}`, {
    method: "DELETE",
  });
  if (!response.ok) {
    throw new Error("Failed to delete task");
  }
}

/**
 * Renders a list of TODO tasks in the task list container,
 * adding a delete button for each.
 * @param {Array} tasks - Array of task objects fetched from the backend.
 */
function renderTaskList(tasks) {
  const taskList = document.getElementById("tasks-list");
  taskList.innerHTML = "";
  tasks.forEach((task) => {
    const taskItem = document.createElement("li");
    taskItem.textContent = `${task.title} ${task.status ? "[Done]" : ""} ${
      task.due_date ? "(Due: " + task.due_date + ")" : ""
    }`;

    // Create Delete button
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.className = "delete-btn";
    deleteBtn.style.marginLeft = "10px";
    deleteBtn.addEventListener("click", async () => {
      if (confirm("Delete this task?")) {
        try {
          await deleteTask(task.id);
          // Remove from UI
          fetchAndDisplayTasks();
        } catch (err) {
          alert("Failed to delete task.");
        }
      }
    });
    taskItem.appendChild(deleteBtn);
    taskList.appendChild(taskItem);
  });
}

/**
 * Shows a temporary loading message in the task list section.
 */
function renderLoadingState() {
  const taskList = document.getElementById("tasks-list");
  taskList.innerHTML = "<li>Loading tasks...</li>";
}

/**
 * Fetches all TODO tasks from the API and displays them in the task list container.
 */
async function fetchAndDisplayTasks() {
  renderLoadingState();
  try {
    const tasks = await getAllTasks();
    renderTaskList(tasks);
  } catch (error) {
    console.error("Error fetching tasks:", error);
    const taskList = document.getElementById("tasks-list");
    taskList.innerHTML = "<li>Error loading tasks</li>";
  }
}

/**
 * Handles the submission of the Add Task form, invokes the API, and updates the list instantly.
 */
document.addEventListener("DOMContentLoaded", function () {
  // Initial fetch to display tasks
  fetchAndDisplayTasks();

  // Form handling
  const addTaskForm = document.getElementById("add-task-form");
  addTaskForm.addEventListener("submit", async function (event) {
    event.preventDefault();
    const titleInput = document.getElementById("task-title");
    const dueDateInput = document.getElementById("task-due-date");
    const title = titleInput.value.trim();
    const due_date = dueDateInput.value;
    if (!title) return; // Should not happen if required, but double check
    const newTaskData = { title };
    if (due_date) {
      newTaskData.due_date = due_date;
    }
    try {
      await createTask(newTaskData);
      // Clear the form
      addTaskForm.reset();
      // Refresh task list
      fetchAndDisplayTasks();
    } catch (error) {
      alert("Failed to add new task.");
      console.error(error);
    }
  });
});
