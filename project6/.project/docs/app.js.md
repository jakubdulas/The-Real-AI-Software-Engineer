# app.js

This is the main entry point of the weather app. It connects the UI with the API and orchestrates user interactions, data fetching, UI updates, and error handling.

## Main Responsibilities
- Handles form submission from the city search input.
- Calls API functions to fetch weather data.
- Updates the UI on successful results.
- Shows error messages on failure or invalid input.

## Detailed Breakdown

### Event: DOMContentLoaded
- Locates the weather form via the `#weather-form` id.
- Attaches a `submit` listener (`handleWeatherFormSubmit`).

### `handleWeatherFormSubmit(event)`
- Prevents default form submit (avoiding reload)
- Reads the city name from the input.
- If no city is entered: does nothing.
- Calls `fetchWeatherData(city)` (from `api.js`): fetches data from OpenWeatherMap API.
    - If successful, constructs the clean weather object and updates the UI via `updateWeatherUI(weatherData)` (from `ui.js`).
    - If there is a problem (invalid city, network, etc), passes the error message to `displayErrorUI()` (from `ui.js`).
- Handles all async logic with async/await.

## Inter-Module Dependencies
- **Uses**
  - `fetchWeatherData` from `js/api.js`
  - `updateWeatherUI`, `displayErrorUI` from `js/ui.js`

## Usage Example (for reference, not run directly)

Relevant app logic is wired automatically when opening `index.html` and does not require direct usage of exported functions.
