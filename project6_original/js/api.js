// js/api.js
// Module to fetch weather data by city name from OpenWeatherMap API
// Exports: getWeatherByCity(cityName)

/**
 * IMPORTANT: For production apps, never expose your real API key in the frontend.
 * For demonstration and local dev, you can use a config setup or placeholder and instruct developers to provide their own key.
 */

const OPENWEATHERMAP_API_BASE =
  "https://api.openweathermap.org/data/2.5/weather";

// TODO: Replace with environment variable in real production usage
const API_KEY = "38f9cf4adfeaa27bb822e30763002a40";

/**
 * Fetch current weather data for a given city from OpenWeatherMap.
 * @param {string} city - The city name to fetch weather for.
 * @returns {Promise<Object>} - Structured weather object or throws error.
 */
export async function getWeatherByCity(city) {
  if (!API_KEY || API_KEY === "YOUR_OPENWEATHERMAP_API_KEY_HERE") {
    throw new Error(
      "API key is missing. Please provide your OpenWeatherMap API key in js/api.js"
    );
  }
  const url = `${OPENWEATHERMAP_API_BASE}?q=${encodeURIComponent(
    city
  )}&appid=${API_KEY}&units=metric`;
  try {
    const res = await fetch(url);
    const data = await res.json();
    if (!res.ok) {
      // OpenWeatherMap sends useful message on error
      throw new Error(data.message || "City not found");
    }
    // Structure the returned data for UI use
    return {
      city: data.name,
      temperature: data.main.temp,
      humidity: data.main.humidity,
      condition: data.weather[0].main, // e.g., "Clouds"
      description: data.weather[0].description, // e.g., "few clouds"
      icon: data.weather[0].icon, // for icon use if needed
    };
  } catch (error) {
    // Network errors or fetch thrown errors
    throw new Error(error.message || "Could not fetch weather data");
  }
}
