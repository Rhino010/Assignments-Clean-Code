class Forecast:
    def __init__(self):
        self.weather_data = {
                                "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
                                "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
                                "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
                            }

    def get_weather(self, city):
        return self.weather_data.get(city, "Weather not available.")
    
    def display_weather(self, city):
        weather = self.get_weather(city)
        print(f"Weather in {city}: {weather['temperature']} degrees, {weather['condition']}, and {weather['humidity']}% humidity. ")