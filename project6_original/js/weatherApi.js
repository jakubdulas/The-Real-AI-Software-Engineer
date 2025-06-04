// js/weatherApi.js
// Module for interacting with the OpenWeatherMap API

const API_KEY = "38f9cf4adfeaa27bb822e30763002a40"; // <-- Replace with your own OpenWeatherMap API key
const BASE_URL = "https://api.openweathermap.org/data/2.5/weather";

/**
 * Fetch current weather data for a given city using OpenWeatherMap API.
 * @param {string} city - City name to fetch weather for
 * @returns {Promise<Object>} Resolves with weather data or error info
 */
export async function getWeather(city) {
  // Build the API endpoint with query parameters
  const url = `${BASE_URL}?q=${encodeURIComponent(
    city
  )}&appid=${API_KEY}&units=metric`;
  try {
    const response = await fetch(url);
    if (!response.ok) {
      // API returns error (e.g., 404 city not found or 401 invalid API key)
      return { error: `City not found or API error: ${response.statusText}` };
    }
    // Parse JSON response
    const data = await response.json();
    return data;
  } catch (error) {
    // Handle network errors
    return { error: "Network error. Please try again." };
  }
}
