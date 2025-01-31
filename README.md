# Telegram Weather Forecast Bot 🌦️

Welcome to the **Telegram Weather Forecast Bot**! This bot provides real-time weather forecasts and alerts users about rain predictions for their specified location. Built using the **Telebot** library and integrated with the **OpenWeatherMap API**, this bot is designed to keep you informed about the weather conditions in your area.

---

## Features

- **Rain Prediction**: Alerts users if rain is expected in the next 12 hours.
- **Real-Time Weather Data**: Fetches weather data from the OpenWeatherMap API.
- **Telegram Integration**: Easy-to-use commands for checking weather forecasts.
- **Lightweight and Efficient**: Built with Flask for seamless deployment.

---

## How It Works

1. **User Command**: Users send the `/weather_forecast` or `/weather` command to the bot.
2. **Location Input**: The bot prompts the user to provide their latitude and longitude.
3. **API Request**: The bot fetches weather data from the OpenWeatherMap API.
4. **Rain Prediction**: The bot checks if rain is expected in the next 12 hours.
5. **Response**: The bot sends a message to the user indicating whether it will rain or not.

---

## Installation

To run this bot locally, follow these steps:

### Prerequisites

- Python 3.8 or higher
- Flask
- Telebot
- OpenWeatherMap API key

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/telegram-weather-bot.git
   cd telegram-weather-bot
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables**:
   Replace the placeholders in the code with your actual API keys:
   ```python
   BOT_API_KEY = 'your_telegram_bot_api_key_here'
   API_KEY = 'your_openweathermap_api_key_here'
   ```

4. **Run the Flask application**:
   ```bash
   python app.py
   ```

---

## Usage

1. Start a chat with your bot on Telegram.
2. Use the `/weather_forecast` or `/weather` command.
3. Provide your latitude and longitude when prompted.
4. Receive a message indicating whether it will rain in the next 12 hours.

---

## Code Overview




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI) for the Telegram bot framework.
- [OpenWeatherMap](https://openweathermap.org/) for the weather data API.
- [Flask](https://flask.palletsprojects.com/) for the lightweight web framework.

---

Stay dry and informed with the Telegram Weather Forecast Bot! 🌧️✨
