// api.js
// Handles fetching weather data from the OpenWeatherMap API.
// Replace 'YOUR_API_KEY' with your actual API key for production use.

const OPENWEATHERMAP_API_KEY = "38f9cf4adfeaa27bb822e30763002a40"; // <-- Insert real API key here for production
const BASE_URL = "https://api.openweathermap.org/data/2.5/weather";

/**
 * Fetches current weather data for a given city using the OpenWeatherMap API.
 * @param {string} cityName - The name of the city to fetch weather for.
 * @returns {Promise<Object>} - A promise that resolves to the weather data JSON.
 * @throws Will throw an error if the network request fails or the city is not found.
 */
async function fetchWeatherData(cityName) {
  if (!cityName) throw new Error("City name is required");

  const url = `${BASE_URL}?q=${encodeURIComponent(
    cityName
  )}&appid=${OPENWEATHERMAP_API_KEY}&units=metric`;

  const response = await fetch(url);
  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    const message = errorData?.message || "Failed to fetch weather data.";
    throw new Error(message);
  }

  const data = await response.json();
  return data;
}
