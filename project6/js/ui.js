// ui.js - Handles UI updates for displaying weather data

/**
 * Update the weather display with given weather data.
 * @param {Object} data - Weather data with fields: city, temperature, humidity, condition, description, icon.
 */
export function updateWeatherDisplay(data) {
    const weatherResult = document.getElementById('weather-result');
    // Create weather display HTML
    weatherResult.innerHTML = `
        <div class="weather-city"><strong>${data.city}</strong></div>
        <div class="weather-main">
            <img src="https://openweathermap.org/img/wn/${data.icon}@2x.png" alt="${data.description}" class="weather-icon">
            <span class="weather-condition">${data.condition}</span>
        </div>
        <div class="weather-details">
            <span class="weather-temp">${data.temperature}&deg;C</span> |
            <span class="weather-humidity">Humidity: ${data.humidity}%</span>
        </div>
        <div class="weather-desc">${data.description}</div>
    `;
}

/**
 * Display a user-friendly error message in the weather result area.
 * Gracefully handles city not found, network issue, and missing data.
 * @param {string} message
 */
export function showError(message) {
    const weatherResult = document.getElementById('weather-result');
    if (message) {
        weatherResult.innerHTML = `
            <div class="weather-error" role="alert" aria-live="polite" tabindex="0">
                <span>⚠️</span> ${message}
            </div>
        `;
    } else {
        // Clear error (for example, when input is cleared)
        weatherResult.innerHTML = '';
    }
}
