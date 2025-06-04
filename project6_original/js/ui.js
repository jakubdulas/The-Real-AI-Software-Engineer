// js/ui.js
// Module for handling UI updates in the weather app

/**
 * Display weather information in the DOM.
 * @param {Object} data - Weather data object from API
 */
export function displayWeather(data) {
  clearWeather();
  clearError();

  // Get the weather result section
  const weatherResult = document.getElementById("weather-result");
  if (!weatherResult) return;

  // Create weather data elements
  const cityElem = document.createElement("h2");
  cityElem.textContent = `${data.name}, ${data.sys.country}`;

  const tempElem = document.createElement("p");
  tempElem.textContent = `Temperature: ${Math.round(data.main.temp)}°C`;

  const humidityElem = document.createElement("p");
  humidityElem.textContent = `Humidity: ${data.main.humidity}%`;

  const condElem = document.createElement("p");
  condElem.textContent = `Condition: ${capitalizeFirst(
    data.weather[0].description
  )}`;

  // Append elements to the weather result section
  weatherResult.appendChild(cityElem);
  weatherResult.appendChild(tempElem);
  weatherResult.appendChild(humidityElem);
  weatherResult.appendChild(condElem);
  weatherResult.style.display = "block";
}

/**
 * Display error message to the user in the DOM.
 * @param {string} message - Error message to display
 */
export function displayError(message) {
  clearWeather();
  const errorElem = document.getElementById("error-message");
  if (errorElem) {
    errorElem.textContent = message;
    errorElem.style.display = "block";
  }
}

/**
 * Clear the weather result display.
 */
export function clearWeather() {
  const weatherResult = document.getElementById("weather-result");
  if (weatherResult) {
    weatherResult.innerHTML = "";
    weatherResult.style.display = "none";
  }
}

/**
 * Clear any error messages from the DOM.
 */
export function clearError() {
  const errorElem = document.getElementById("error-message");
  if (errorElem) {
    errorElem.textContent = "";
    errorElem.style.display = "none";
  }
}

/**
 * Capitalize the first letter of a string.
 * @param {string} str
 * @returns {string}
 */
function capitalizeFirst(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}
