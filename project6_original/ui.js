// ui.js

/**
 * Updates the UI area with fetched weather information.
 * @param {Object} data - Weather data containing temperature, humidity, and conditions.
 * @param {number} data.temperature - Temperature in Celsius.
 * @param {number} data.humidity - Humidity percentage.
 * @param {string} data.condition - Weather condition description (e.g., 'Cloudy').
 */
export function updateWeatherUI({ temperature, humidity, condition }) {
  const resultDiv = document.querySelector('.weather-result');
  if (!resultDiv) return;

  resultDiv.innerHTML = `
    <div class="weather-info">
      <div><strong>Temperature:</strong> ${temperature}&deg;C</div>
      <div><strong>Humidity:</strong> ${humidity}%</div>
      <div><strong>Condition:</strong> ${condition}</div>
    </div>
  `;
}

/**
 * Displays a user-friendly error message in the weather result UI area.
 * @param {string} message - The error message to display.
 */
export function displayErrorUI(message) {
  const resultDiv = document.querySelector('.weather-result');
  if (!resultDiv) return;
  resultDiv.innerHTML = `<div class="weather-error">${message}</div>`;
}

