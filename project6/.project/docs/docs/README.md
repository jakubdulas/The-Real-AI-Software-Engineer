# Weather App

A simple, frontend-only web application that fetches and displays current weather data for any city using the OpenWeatherMap API. The app is built using HTML, CSS, and modular JavaScript, and works entirely in the browser with no backend dependencies.

---

## Features
- **City Search**: Enter the name of any city worldwide to get the current weather.
- **Weather Details**: Displays temperature, humidity, and a short description of weather conditions (e.g., "Cloudy", "Sunny").
- **Error Handling**: Graceful error messages for invalid city names, network problems, or API errors.
- **Modular Code**: JavaScript split into modules for API communication and UI updates.

---

## File/Code Structure

```
|-- index.html              # App UI and container elements
|-- styles.css              # All app styling
|-- js/
|   |-- app.js              # Main entry point, user interaction wiring
|   |-- weatherApi.js       # API interaction module
|   |-- ui.js               # UI rendering and error handling
|-- docs/
|   |-- README.md           # This documentation
```

---

## How to Use

1. **Obtain an API Key:**
   - Sign up on [OpenWeatherMap](https://openweathermap.org/) to get a free API key.
2. **Configure API Key:**
   - Open `js/weatherApi.js` and replace `'YOUR_OPENWEATHERMAP_API_KEY'` with your actual API key.
     ```js
     const API_KEY = 'YOUR_REAL_API_KEY_HERE';
     ```
3. **Open the App:**
   - Open `index.html` directly in your browser (no server needed).
4. **Search for Weather:**
   - Enter the city name in the input and click "Get Weather".
   - View the weather information or error message if the city is not found.

---

## Module/File Explanations

### index.html
Defines the app structure: a title, a city input form, and display sections for errors and weather results. Loads CSS and the main JavaScript module on page load.

- **Form**: `<form id="weather-form">` for user input
- **Display**: Divs with ids `weather-result` and `error-message` for output
- **Entry Point**: Loads `js/app.js` as JS module

---

### styles.css
All styles for layout and appearance. Styles elements including the input form, container, and display areas for weather and errors.

---

### js/app.js
Main entry point. Handles user events, collects city input, calls the API module, and routes data/results to the UI module.
- **Imports**: `getWeather` (from `weatherApi.js`) and UI functions (`displayWeather`, `displayError`)
- **Behavior**:
  - Listens for form submissions
  - Calls `getWeather(city)`
  - Shows results or errors using UI helper functions

---

### js/weatherApi.js
Handles all communication with the weather API.
- Define your OpenWeatherMap API key at the top
- Exports one function:
  - `getWeather(city)`: Async, returns the parsed weather JSON or standardized error object. Handles HTTP and network errors gracefully.

---

### js/ui.js
Handles DOM manipulation to render results or errors.
- `displayWeather(data)`: Shows weather info in the UI for the given city/data
- `displayError(message)`: Renders an error message
- `clearWeather()`, `clearError()`: Helper functions to clear previous results/errors

---

## Troubleshooting
- **CORS**: If you run into CORS errors locally, try serving the files with a simple HTTP server (`python -m http.server`, `npx serve`, etc).
- **API Limits**: Free API keys have some restrictions and rate limits.
- **City Not Found**: Entered city must be spelled correctly; if not found, a user-friendly message will display.

---

## License
This project is released under the MIT License.
