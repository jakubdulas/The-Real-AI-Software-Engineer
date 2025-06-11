// main.js - Handles city input, form submission, calls weather API, processes result
import { getWeatherByCity } from './api.js';
import { updateWeatherDisplay, showError } from './ui.js';

// Element selectors
document.addEventListener('DOMContentLoaded', () => {
    const cityForm = document.getElementById('city-form');
    const cityInput = document.getElementById('city-input');

    // Handle city form submit
    cityForm.addEventListener('submit', async (e) => {
        e.preventDefault(); // Prevent page reload
        const city = cityInput.value.trim();
        if (!city) {
            showError('Please enter a city name.');
            return;
        }
        try {
            // Call weather API module
            const weatherData = await getWeatherByCity(city);
            // Handle response (for now pass to dummy display)
            updateWeatherDisplay(weatherData);
        } catch (error) {
            // Handle error
            showError(error.message || 'Unable to fetch weather.');
        }
    });
});
