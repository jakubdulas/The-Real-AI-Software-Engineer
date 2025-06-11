// inputHandler.js - Handles user input events and API invocation
import { getWeatherByCity } from './api.js';

/**
 * Simple debounce helper
 */
function debounce(fn, delay) {
    let timer = null;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), delay);
    };
}

/**
 * Attaches event handlers for submit and input to the city field and form.
 * @param {{onSuccess: function, onError: function}} callbacks 
 */
export function attachCityInputHandler(callbacks) {
    document.addEventListener('DOMContentLoaded', () => {
        const cityForm = document.getElementById('city-form');
        const cityInput = document.getElementById('city-input');

        // Submit handler
        cityForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const city = cityInput.value.trim();
            if (!city) {
                callbacks.onError('Please enter a city name.');
                return;
            }
            try {
                const weatherData = await getWeatherByCity(city);
                callbacks.onSuccess(weatherData);
            } catch (error) {
                callbacks.onError(error.message || 'Unable to fetch weather.');
            }
        });

        // Debounced input handler: fires when user stops typing (after 500 ms)
        cityInput.addEventListener('input', debounce(async (e) => {
            const city = e.target.value.trim();
            if (!city) {
                callbacks.onError(''); // clear errors if empty
                return;
            }
            try {
                const weatherData = await getWeatherByCity(city);
                callbacks.onSuccess(weatherData);
            } catch (error) {
                callbacks.onError(error.message || 'Unable to fetch weather.');
            }
        }, 500));
    });
}
