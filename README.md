# Simple Weather App

## 🚀 Project Title
Command-Line Weather App with Colorful Output

## 🎯 Objective
Create a simple command-line Python application that fetches and displays current weather information for a user-specified city using the OpenWeatherMap API.

## 🛠 Tools and Technologies Used
- Python 3.x
- requests (for API calls)
- colorama (for colored terminal output)
- OpenWeatherMap API

## 📋 Features Implemented
- Fetch current weather data for any city.
- Display temperature in Celsius, humidity, and weather condition.
- Use color-coded output to enhance readability.
- Handle invalid city names or API errors gracefully.

## 💡 How to Use
1. Run the Python script.
2. Enter the city name when prompted.
3. View the current weather details printed in the terminal.

## 🛠 Setup Instructions
1. Install Python 3.x from [python.org](https://www.python.org/downloads/).
2. Install the required Python packages:
    ```bash
    pip install requests colorama
    ```
3. Obtain a free API key from [OpenWeatherMap](https://openweathermap.org/api) by creating an account.
4. Replace the `API_KEY` value in the script with your actual API key.
5. Run the script:
    ```bash
    python weather_app.py
    ```
6. When prompted, enter a city name to get the weather information.

## 🔍 Project Description
This project connects to the OpenWeatherMap API to retrieve real-time weather information. The app outputs temperature, humidity, and weather conditions in a color-coded format for better clarity in the terminal. It serves as an introductory project for learning API integration, JSON parsing, and terminal UI enhancement with Python.

## ✅ Outcome
A working command-line weather app that:
- Retrieves live weather data.
- Presents data clearly with colors.
- Manages errors like incorrect city names or API issues.

## 🧠 Learning Experience
- Making HTTP requests and parsing JSON data in Python.
- Using the colorama library for colored terminal output.
- Handling user input and errors effectively.
- Working with a real-world REST API.
