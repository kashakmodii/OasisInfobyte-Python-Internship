import requests
def get_weather(city):
    api_key = "439d4b804bc8187953eb36d2a8c26a02"  # Built-in key from openweathermap
    url = f"https://openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("cod") == 200:
            print(f"\nWeather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Conditions: {data['weather'][0]['description']}")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data.get('message', 'Unknown error')}")
    
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")

print("🌦️ Simple Weather App 🌞")
print("----------------------")
while True:
    city = input("\nEnter city name (or 'quit' to exit): ").strip()
    if city.lower() == 'quit':
        break
    get_weather(city)
print("\nThanks for using the weather app!")
