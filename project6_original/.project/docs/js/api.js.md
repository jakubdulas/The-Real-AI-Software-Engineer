# js/api.js

This module handles all communication with the OpenWeatherMap API for fetching current weather data. It encapsulates the API request logic and error handling, exposing a single asynchronous function for use throughout the app.

## Exports

### `fetchWeatherData(cityName)`

Fetches the current weather data for a given city from the OpenWeatherMap API.

#### Parameters:
- `cityName` (`string`): The name of the city for which the weather should be fetched.

#### Returns:
- `Promise<Object>`: Resolves to the JSON object returned by the OpenWeatherMap API containing weather data.

#### Throws:
- Will throw an error if the city is not found, the API request fails, or the city name is empty.

#### Example:
```js
import { fetchWeatherData } from './api.js';

fetchWeatherData('Warsaw')
  .then(data => {
    // Use weather data
  })
  .catch(error => {
    // Handle error
  });
```

#### API Key
> **Note:** Replace `'YOUR_API_KEY'` in the source file with your actual OpenWeatherMap API key for production use. The app will not work without a valid API key.

#### Structure of API Data (Typical Example)
- `main.temp`: Current temperature (°C)
- `main.humidity`: Humidity (%)
- `weather[0].description`: Weather conditions (e.g., "Cloudy", "Sunny")

#### Internal Details:
- The endpoint used: `https://api.openweathermap.org/data/2.5/weather`
- Requests use the `units=metric` parameter for Celsius temperature.
- Handles error responses gracefully by parsing the message (e.g., for city not found) and returning a user-friendly error.