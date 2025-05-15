Oto propozycje promptów do stworzenia każdego z 6 projektów w ramach Twojego systemu wieloagentowego. Każdy prompt jest zaprojektowany tak, by maksymalnie precyzyjnie nakierować agenta na stworzenie kompletnego, zgodnego z założeniami projektu.

---

## 🧮 **Simple Console Applications**

### ✅ **Project 1 Prompt – Temperature Converter (Single-file)**

```
Write a simple console-based temperature converter in a single Python file. The program should:
- Allow the user to input a numeric value and select the unit (Celsius, Fahrenheit, or Kelvin),
- Convert the input value to the two remaining units,
- Validate the input (handle invalid numbers or units),
- Display the converted values clearly in the terminal.

Everything must be implemented in a single file named `converter.py`. Make the code clean, readable, and testable (define a reusable function like `convert(value, from_unit, to_unit)`).
```

---

### ✅ **Project 2 Prompt – CLI Note Manager (Multi-file)**

```
Create a command-line note manager in Python. The application should:
- Allow users to create, delete, and view notes from a terminal menu,
- Each note should have a title, content, and timestamp,
- Store notes persistently in a JSON file,
- Use a modular structure with at least four files:
  - `main.py`: for the user interface and menu logic,
  - `note.py`: a class representing a Note,
  - `storage.py`: handles saving and loading notes to/from a file,
  - `utils.py`: optional helper functions.

Include basic input validation and clean separation between logic and user interaction.
```

---

## 🎮 **Games**

### ✅ **Project 3 Prompt – Tic Tac Toe (Console)**

```
Build a terminal-based Tic Tac Toe game in Python. The game should:
- Allow two human players to take turns OR one player to play against a simple AI,
- Display the board after each move using ASCII,
- Validate player input (e.g., disallow overwriting occupied cells),
- Detect wins and draws and end the game accordingly,
- Use modular code: ideally include classes or functions for Player, Board, Game Logic, and AI (even in a single file).

Include comments and structure the code to be easy to extend.
```

---

### ✅ **Project 4 Prompt – Snake Game (Pygame GUI)**

```
Create a Snake game using Pygame. The game should:
- Render a visual grid with a snake that moves based on arrow key input,
- Include an apple that randomly spawns on the grid; the snake grows after eating it,
- Detect collisions with walls or itself and end the game accordingly,
- Display the player's score,
- Organize the code into logical components: game loop, rendering, input handling, and collision logic.

Make the code modular and readable. Include a `requirements.txt` file if external libraries are needed.
```

---

## 🌐 **Web Applications**

### ✅ **Project 5 Prompt – TODO List App (Backend + Frontend)**

```
Create a web-based TODO list application consisting of:
1. A backend REST API using Flask, Django REST Framework, or FastAPI. The API should support:
   - Creating, reading, updating, and deleting TODO items,
   - Each task has a title, status (done or not), and optional due date,
   - Endpoints: `GET /tasks`, `POST /tasks`, `PATCH /tasks/{id}`, `DELETE /tasks/{id}`.

2. A basic frontend (HTML + JavaScript) that:
   - Lists all tasks,
   - Allows adding and deleting tasks via API calls (e.g., using `fetch`),
   - Uses minimal styling.

Keep backend and frontend code in separate directories (`backend/`, `frontend/`). Document how to run the project locally.
```

---

### ✅ **Project 6 Prompt – Weather App (Frontend + API integration)**

```
Create a simple frontend-only weather app using HTML, CSS, and JavaScript. The app should:
- Allow the user to input a city name,
- Fetch current weather data for that city using the OpenWeatherMap API (or another public weather API),
- Display information such as temperature, humidity, and weather conditions (e.g., "Cloudy", "Sunny"),
- Use modular JavaScript (e.g., separate files or functions for API requests and UI updates),
- Handle invalid city names gracefully (e.g., display an error message if the city is not found).

Do not use any backend – the app should work entirely in the browser.
```

---

Chcesz, żebym teraz wygenerował np. "idealne rozwiązanie" jednego z tych promptów, żebyś mógł użyć jako wzorca dla Levenshteina czy testów porównawczych?
