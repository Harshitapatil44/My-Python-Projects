import requests


def weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n Weather in {city_name.title()}:")
        print(f" Condition: {weather}")
        print(f" Temperature: {temp}°C")
        print(f" Humidity: {humidity}%")
        print(f" Wind Speed: {wind_speed} m/s\n")
    else:
        print(" City not found or API error.")


def main():
    print("=== Weather App ===")
    api_key = "My_weather_app_api_key_here"
    city = input("Enter city name: ")
    weather(city, api_key)


if __name__ == "__main__":
    main()
