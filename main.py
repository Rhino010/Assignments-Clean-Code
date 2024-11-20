from forecast import Forecast

def main():
    current_weather = Forecast()

    city_name = input("Please enter the city name you would like the weather for.")

    current_weather.display_weather(city_name)

if __name__ == "__main__":
    main()