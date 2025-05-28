# js/ui.js

This module is responsible for updating and managing the User Interface (UI) of the weather app. It provides functions to display current weather information and to show errors in a user-friendly manner.

## Exports

### `updateWeatherUI({ temperature, humidity, condition })`

Updates the designated UI area to display weather data 

#### Parameters:
- `temperature` (`number`): Temperature in Celsius
- `humidity` (`number`): Relative humidity (%)
- `condition` (`string`): Human-readable weather description (e.g., "Cloudy")

#### Functionality:
- locates the element with class `.weather-result`
- injects HTML showing temperature, humidity, and condition
- does nothing if the UI area is missing

#### Example:
```js
import { updateWeatherUI } from './ui.js';
updateWeatherUI({ temperature: 12, humidity: 65, condition: 'Clear sky' });
```

### `displayErrorUI(message)`

Displays an error message to the user in the weather result UI area.

#### Parameters:
- `message` (`string`): Text of the error message

#### Functionality:
- locates the `.weather-result` element
- displays a prominent stylized error
- nothing happens if the area is missing

#### Example:
```js
import { displayErrorUI } from './ui.js';
displayErrorUI('City not found. Please enter a valid city name.');
```
