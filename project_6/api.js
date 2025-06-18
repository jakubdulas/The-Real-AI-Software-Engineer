// api.js
// Handles interaction with the weather API (OpenWeatherMap)

const OPENWEATHERMAP_API_KEY = "38f9cf4adfeaa27bb822e30763002a40"; // Replace with your OpenWeatherMap API key
const BASE_URL = "https://api.openweathermap.org/data/2.5/weather";

/**
 * Fetch current weather data for a given city from OpenWeatherMap API.
 * @param {string} city - City name
 * @returns {Promise<{success: boolean, data?: object, error?: string}>}
 */
export async function fetchWeatherData(city) {
  const url = `${BASE_URL}?q=${encodeURIComponent(
    city
  )}&appid=${OPENWEATHERMAP_API_KEY}&units=metric`;
  try {
    const response = await fetch(url);
    const data = await response.json();
    if (!response.ok) {
      let errorMsg =
        data && data.message ? data.message : "Failed to fetch weather data.";
      return { success: false, error: errorMsg };
    }
    return { success: true, data };
  } catch (error) {
    return { success: false, error: "Network error. Please try again." };
  }
}
