import requests
import pandas as pd
import matplotlib.pyplot as plt

city = "Mianwali"
api_key = "c1716de7a8ee8e04e5a0fa441b2dccc5"  # Your API key

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
        return None

def process_weather_data(weather_data):
    forecast_list = weather_data['list']
    
    data = {
        "datetime": [],
        "temperature": [],
        "humidity": [],
        "weather": []
    }
    
    for entry in forecast_list:
        data["datetime"].append(entry['dt_txt'])
        data["temperature"].append(entry['main']['temp'])
        data["humidity"].append(entry['main']['humidity'])
        data["weather"].append(entry['weather'][0]['description'])
    
    return pd.DataFrame(data)

def plot_weather_data(weather_df):
    plt.figure(figsize=(14, 7))
    
    plt.subplot(2, 1, 1)
    plt.plot(weather_df['datetime'], weather_df['temperature'], label='Temperature (°C)', color='orange')
    plt.xticks(rotation=45)
    plt.title('Temperature Over Time')
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°C)')
    plt.grid(True)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(weather_df['datetime'], weather_df['humidity'], label='Humidity (%)', color='blue')
    plt.xticks(rotation=45)
    plt.title('Humidity Over Time')
    plt.xlabel('Date & Time')
    plt.ylabel('Humidity (%)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Fetch and process data
weather_data = fetch_weather_data(city, api_key)

if weather_data:
    weather_df = process_weather_data(weather_data)
    plot_weather_data(weather_df)
