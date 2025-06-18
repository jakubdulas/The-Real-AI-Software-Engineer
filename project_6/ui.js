// ui.js
// Handles updating the UI with weather data or errors

/**
 * Updates the weather display with the given weather data.
 * @param {Object} weatherData - The weather data object.
 *   Should contain: city, temperature, humidity, description.
 */
export function updateWeatherUI(weatherData) {
  const weatherDis = document.getElementById("weather-display");
  const cityElem = document.getElementById("weather-city");
  const tempElem = document.getElementById("weather-temp");
  const humidityElem = document.getElementById("weather-humidity");
  const errorElem = document.getElementById("error-message");

  weatherDis.style.display = "block";
  // Hide error message if visible
  if (errorElem) {
    errorElem.textContent = "";
    errorElem.style.display = "none";
  }
  if (cityElem && tempElem && humidityElem) {
    cityElem.textContent = weatherData.name;
    tempElem.textContent = `${weatherData.main.temp}`;
    humidityElem.textContent = `${weatherData.main.humidity}`;
  }
}

/**
 * Shows an error message in the UI.
 * @param {string} message - The error message to display.
 */
export function showError(message) {
  const errorElem = document.getElementById("error-message");

  if (errorElem) {
    errorElem.textContent = message;
    errorElem.style.display = "block";
  }
}
