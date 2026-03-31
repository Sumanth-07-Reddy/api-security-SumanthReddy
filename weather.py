import os
import requests
from dotenv import load_dotenv

# Load environment variables securely
load_dotenv()

# Task 1: API key is loaded from .env (never hardcoded)
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY not found in .env file. Please add your key and try again.")

def get_weather_alert(city: str):
    """
    Fetch weather data and show alerts for clinic patients.
    """
    # Task 3: Privacy protection
    # We do NOT log the searched city name. Location data in a healthcare context
    # is considered sensitive personal information. Logging it could violate 
    # GDPR (data minimization and purpose limitation principles) and healthcare 
    # privacy regulations like HIPAA.

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=10)
        
        # Task 2: Handle rate limiting gracefully
        if response.status_code == 429:
            print("Rate limit exceeded (60 calls/min on free tier). Please wait before trying again.")
            return None
            
        if response.status_code != 200:
            print(f"Error fetching weather: {response.status_code}")
            return None
            
        data = response.json()
        
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        
        print(f"Current weather: {temp}°C, {desc}")
        
        if temp < 5:
            print("⚠️ Cold weather alert: Advise patients to stay warm.")
        elif temp > 35:
            print("⚠️ Heat weather alert: Advise patients to stay hydrated.")
            
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
