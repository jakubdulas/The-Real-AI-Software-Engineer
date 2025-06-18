// ui.js
// Handles updating the UI with weather data or errors

/**
 * Updates the weather display with the given weather data.
 * @param {Object} weatherData - The weather data object.
 *   Should contain: city, temperature, humidity, description.
 */
export function updateWeatherUI(weatherData) {
  const cityElem = document.getElementById('weather-city');
  const tempElem = document.getElementById('weather-temp');
  const humidityElem = document.getElementById('weather-humidity');
  const descElem = document.getElementById('weather-desc');
  const errorElem = document.getElementById('error-message');

  // Hide error message if visible
  if (errorElem) {
    errorElem.textContent = '';
    errorElem.style.display = 'none';
  }
  if (cityElem && tempElem && humidityElem && descElem) {
    cityElem.textContent = weatherData.city;
    tempElem.textContent = `${weatherData.temperature} °C`;
    humidityElem.textContent = `${weatherData.humidity} %`;
    descElem.textContent = weatherData.description;
  }
}

/**
 * Shows an error message in the UI.
 * @param {string} message - The error message to display.
 */
export function showError(message) {
  const errorElem = document.getElementById('error-message');
  const cityElem = document.getElementById('weather-city');
  const tempElem = document.getElementById('weather-temp');
  const humidityElem = document.getElementById('weather-humidity');
  const descElem = document.getElementById('weather-desc');

  if (errorElem) {
    errorElem.textContent = message;
    errorElem.style.display = 'block';
  }
  // Optionally clear weather info when showing error
  if (cityElem) cityElem.textContent = '';
  if (tempElem) tempElem.textContent = '';
  if (humidityElem) humidityElem.textContent = '';
  if (descElem) descElem.textContent = '';
}
