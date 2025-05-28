// Event handler for form submission
async function handleWeatherFormSubmit(event) {
  event.preventDefault();
  const cityInput = document.getElementById("city-input");
  if (!cityInput) return;
  const city = cityInput.value.trim();
  if (!city) return;

  try {
    const apiResp = await fetchWeatherData(city);
    // Parse API response into the structure expected by updateWeatherUI
    const weatherData = {
      temperature: Math.round(apiResp.main.temp),
      humidity: apiResp.main.humidity,
      condition: apiResp.weather[0].description,
    };
    updateWeatherUI(weatherData);
  } catch (error) {
    displayErrorUI(
      error.message || "City not found. Please enter a valid city name."
    );
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const weatherForm = document.getElementById("weather-form");
  if (weatherForm) {
    weatherForm.addEventListener("submit", handleWeatherFormSubmit);
  }
});
