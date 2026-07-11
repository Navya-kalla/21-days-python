import requests
from config import API_KEY
import json


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def save_history(weather):
    history = {
        "city": weather["name"],
        "temperature": weather["main"]["temp"],
        "humidity": weather["main"]["humidity"],
        "wind_speed": weather["wind"]["speed"],
        "description": weather["weather"][0]["description"]
    }
    try:
        with open("weather_history.json",'r') as file:
            data = json.load(file)
    except:
        data =[]
    data.append(history)
    with open("weather_history.json",'w') as file:
        json.dump(data,file,indent=4)

def view_history():
    try:
        with open("weather_history.json",'r') as file:
            data = json.load(file)

        if len(data) == 0:
            print("No history found!")
            return

        print("======SEARCH HISTORY======")
        for record in data:
            print(f"City        : {record['city']}")
            print(f"Temperature : {record['temperature']} °C")
            print(f"Humidity    : {record['humidity']} %")
            print(f"Wind Speed  : {record['wind_speed']} m/s")
            print(f"Condition   : {record['description']}")
            print("-" * 35)
    except:
        print("\n No History Found!!")

def display_weather(weather):
    print("="*40)
    print("     WEATHER DASHBOARD")
    print("="*40)
    print("City:", weather["name"])
    print("Temperature:", weather["main"]["temp"], "°C")
    print("Feels Like:", weather["main"]["feels_like"], "°C")
    print("Humidity:", weather["main"]["humidity"], "%")
    print("Wind Speed:", weather["wind"]["speed"], "m/s")
    print("Condition:", weather["weather"][0]["description"])
    print("=" * 40)

while True:
    print("""`====WEATHER DASHBOARD====
1. Search Weather
2.View History
3. Exit""")
    try:
        choice = int(input("Enter choice: "))
        if choice ==1:
            city = input("Enter city: ")
            weather = get_weather(city)
            if weather["cod"] != 200:
                print("City not found!")
                continue
            display_weather(weather)
            save_history(weather)
        
        elif choice == 2:
            view_history()

        elif choice == 3:
            print("Thank you for using Weather Dashboard!")
            break
        else:
            print("Invalid choice!")
    except:
        print("Please enter valid number!!")

