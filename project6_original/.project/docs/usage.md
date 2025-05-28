# Simple Weather App &mdash; Usage Guide

## Overview
This single-page web application provides live weather information for any city, using the OpenWeatherMap API. The app is entirely frontend-based (runs in your browser), implemented with HTML, CSS, and modular JavaScript.

## Features
- **Search for any city:** Enter a city name and retrieve current weather conditions.
- **View weather details:** See the city's current temperature, humidity, and a human-readable weather description.
- **Clear UI:** Modern, responsive interface with user-friendly error handling for unknown cities.

---

## Getting Started

### 1. Prerequisites
- A web browser (Chrome, Firefox, Edge, Safari, etc)
- An OpenWeatherMap API key (sign up at https://openweathermap.org/api for free)

### 2. Project Structure
```
index.html
style.css
app.js
js/
  api.js
  ui.js
```

### 3. Setting Up the API Key
1. Open `js/api.js` in a text/code editor.
2. Replace `'YOUR_API_KEY'` with your own OpenWeatherMap API key:
   ```js
   const OPENWEATHERMAP_API_KEY = 'your_real_api_key_here';
   ```
3. Save the file.

### 4. Running the App
Just open `index.html` **directly in your browser**. No build steps or server are needed!

---

## How to Use
1. **On page load**, you'll see a search bar with a "Weather App" title.
2. **Enter a city name** (e.g., "London" or "San Francisco").
3. **Click "Search"** or press `Enter`.
4. **Weather data will appear** below, showing temperature, humidity, and weather conditions.
5. **If the city name is invalid**, an error message will appear.

---

## File Documentation
- `js/api.js`: Handles all API requests to OpenWeatherMap. Throws clear errors on failure.
- `js/ui.js`: Updates the web page with weather data or friendly errors.
- `app.js`: Orchestrates user interaction, coordinates API/UI updates.

Refer to each file's `.md` documentation for in-depth details!

## Troubleshooting
- **Nothing happens / no data:** Make sure you set a valid API key in `js/api.js`.
- **CORS error:** OpenWeatherMap supports browser requests, but check your network if issues persist.
- **City not found:** Check spelling; some cities may have multiple matches — try adding country (e.g., `Paris, FR`).

## License
This app is for demonstration and educational use.
