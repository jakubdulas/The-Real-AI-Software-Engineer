# Weather App

A simple frontend-only weather application built with HTML, CSS, and JavaScript. This application allows users to check the current weather conditions for any city using live data from the OpenWeatherMap API.

---

## Features

- **Live weather details:** View current temperature, humidity, and weather condition (e.g., "Cloudy", "Sunny") for any valid city.
- **Intuitive interface:** Clean, user-friendly design.
- **Input validation:** Ensures users enter a valid city name.
- **Error handling:** Clear error messages if a city is not found or in case of API/network issues.
- **Frontend only:** No backend required; all functionality runs in your browser.

---

## Requirements

- **Web browser:** A modern browser (Chrome, Firefox, Safari, Edge, etc.)
- **API Key:**
  - You need a free API key from [OpenWeatherMap](https://openweathermap.org/api).
    1. Go to the [OpenWeatherMap Signup Page](https://home.openweathermap.org/users/sign_up).
    2. Register for a free account and obtain your API key from your dashboard.
  - Insert your API key in the appropriate place within the JavaScript (see the documentation in the code for details, usually a line like: `const API_KEY = 'YOUR_API_KEY_HERE';`).

---

## How to Use

1. **Open the App:**
   - Open the `index.html` file in your web browser.
2. **Enter a City Name:**
   - Type the name of the city you want the weather for into the input box.
   - (Tip: Use the city’s common English name, e.g., `London`, `New York`, `Tokyo`)
3. **Submit:**
   - Click the "Search" or "Get Weather" button to check the weather.
4. **View the Results:**
   - The current temperature (in Celsius or Fahrenheit), humidity, and conditions will be shown below the form.
5. **Error Handling:**
   - If you enter an invalid city or there’s a network/API issue, a clear error message will be displayed.
   - Check spelling and internet connection if you receive an error.

---

## Tips & Troubleshooting

- You **must** supply your own API key for the app to function.
- Some less-common or misspelled city names may not be found—double-check your input.
- API response time and limits depend on your OpenWeatherMap account type—free accounts have a rate limit.
- If you change the API key or run into problems, try reloading the page.

---

## License

This is an educational/demo project. You are free to modify, enhance, and use it as you wish.