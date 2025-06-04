// js/app.js
// Entry point: wires input, button, and modules. Handles user actions and orchestrates UI updates.
import { getWeather } from "./weatherApi.js";
import {
  displayWeather,
  displayError,
  clearError,
  clearWeather,
} from "./ui.js";

document.addEventListener("DOMContentLoaded", () => {
  // Get references to form and input elements
  const form = document.getElementById("weather-form");
  const input = document.getElementById("city-input");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const city = input.value.trim();
    if (!city) {
      // Input validation: require a city name
      displayError("Please enter a city name.");
      return;
    }
    // Optionally clear previous outputs before loading
    clearWeather();
    clearError();
    // Fetch weather data for entered city
    const result = await getWeather(city);
    if (result.error) {
      // Handle network or API request error
      displayError(result.error);
    } else if (result.cod && +result.cod !== 200) {
      // OpenWeatherMap can return e.g. { cod: "404", message: "city not found" }
      displayError(result.message || "City not found.");
    } else {
      // Successful fetch: display weather data
      displayWeather(result);
    }
  });
});
