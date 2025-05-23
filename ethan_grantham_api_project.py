import requests 

# This script retrieves weather data from the WeatherAPI using a given API key and location (zip code or city name).
enter_into_api_key = input("Enter Zip Code or City Name: ")
api_key = f"http://api.weatherapi.com/v1/current.json?key=5e53451fdeef415d9fe215846251104&q={enter_into_api_key}&aqi=no"
r_response = requests.get(api_key)


# This function retrieves weather data from the API. If the request is successful, it returns the weather data in JSON format.
# If the request fails, it prints an error message with the status code.
def get_weather_data(name):
    if r_response.status_code == 200:
        print(f"Success. Listing current location for {enter_into_api_key}...")
        weather_data = r_response.json()
        return weather_data
    else:
        print(f"Request failed with status code: {r_response.status_code}")


weather_name = "current weather"
weather_info = get_weather_data(weather_name)

if weather_info:
    # Uncomment the lines below to print all the information    
    print(f"{weather_info['location']['name']}")
    print(f"{weather_info['location']['region']}")
    print(f"{weather_info['location']['country']}")
    print(f"{weather_info['location']['lat']}")
    print(f"{weather_info['location']['lon']}")
    print(f"{weather_info['location']['tz_id']}")
    print(f"{weather_info['location']['localtime']}")
    #print(f"{weather_info['location']['localtime_epoch']}")
    #print(f"{weather_info['current']['temp_c']}")
    print(f"{weather_info['current']['temp_f']}")
    print(f"{weather_info['current']['is_day']}")
    print(f"{weather_info['current']['condition']['text']}")
    #print(f"{weather_info['current']['condition']['icon']}")
    #print(f"{weather_info['current']['condition']['code']}")
    #print(f"{weather_info['current']['wind_mph']}")
    #print(f"{weather_info['current']['wind_kph']}")
    #print(f"{weather_info['current']['wind_degree']}")
    #print(f"{weather_info['current']['wind_dir']}")
    #print(f"{weather_info['current']['pressure_mb']}")
    #print(f"{weather_info['current']['pressure_in']}")
    #print(f"{weather_info['current']['precip_mm']}")
    #print(f"{weather_info['current']['precip_in']}")
    #print(f"{weather_info['current']['humidity']}")
    #print(f"{weather_info['current']['cloud']}")
    #print(f"{weather_info['current']['feelslike_c']}")
    #print(f"{weather_info['current']['feelslike_f']}")
    #print(f"{weather_info['current']['vis_km']}")
    #print(f"{weather_info['current']['vis_miles']}")
    #print(f"{weather_info['current']['uv']}")
    #print(f"{weather_info['current']['gust_mph']}")
    #print(f"{weather_info['current']['gust_kph']}")
    #print(f"{weather_info['current']['air_quality']['co']}")
    #print(f"{weather_info['current']['air_quality']['no2']}")
    #print(f"{weather_info['current']['air_quality']['o3']}")
    #print(f"{weather_info['current']['air_quality']['so2']}")
    #print(f"{weather_info['current']['air_quality']['pm2_5']}")
    #print(f"{weather_info['current']['air_quality']['pm10']}")
    #print(f"{weather_info['current']['air_quality']['us-epa-index']}")
    #print(f"{weather_info['current']['air_quality']['gb-defra-index']}")
    #print(f"{weather_info['current']['last_updated']}")
    #print(f"{weather_info['current']['last_updated_epoch']}")
