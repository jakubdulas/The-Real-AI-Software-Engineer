import { fetchWeatherData } from "./api.js";
import { updateWeatherUI, showError } from "./ui.js";

// DOM elements
const form = document.getElementById("weather-form");
const cityInput = document.getElementById("city-input");

/**
 * Validate the city input according to rules:
 * - Not empty
 * - Only letters, spaces, and hyphens permitted
 * Returns { valid: boolean, error: string|null }
 */
function validateCityInput(city) {
  if (!city) {
    return { valid: false, error: "Please enter a city name." };
  }
  // Unicode letters, spaces, apostrophes, hyphens allowed
  const validPattern = /^[\p{L} .'-]+$/u;
  if (!validPattern.test(city)) {
    return {
      valid: false,
      error:
        "Please use only letters, spaces, apostrophes, or hyphens in city names.",
    };
  }
  return { valid: true, error: null };
}

// Event listener for form submission
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const city = cityInput.value.trim();
  const validation = validateCityInput(city);
  if (!validation.valid) {
    showError(validation.error);
    return;
  }

  showError("");

  try {
    const result = await fetchWeatherData(city);
    if (result.success) {
      updateWeatherUI(result.data);
    } else {
      showError(result.error || "City not found.");
    }
  } catch (err) {
    showError("Failed to fetch weather data. Please try again later.");
  }
});
