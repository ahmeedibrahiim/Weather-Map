import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(lat, lon):
    api_key = "97794765406e651526df5bbf886d903f"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def search_weather():
    location = ent_location.get()
    if location.lower() == "cairo":
        lat, lon = 30.03333, 31.233334
    else:
        messagebox.showerror("Error", "Location not supported.")
        return

    weather_data = get_weather(lat, lon)
    if weather_data:
        temp = weather_data['current']['temp'] - 273.15  
        humidity = weather_data['current']['humidity']
        wind_speed = weather_data['current']['wind_speed']
        pressure = weather_data['current']['pressure']
        precipitation = weather_data.get('daily', [{}])[0].get('rain', 0)
        print(precipitation)

        result_text = (f"Temperature: {temp:.2f}°C\n"
                       f"Humidity: {humidity}%\n"
                       f"Wind Speed: {wind_speed} m/s\n"
                       f"Pressure: {pressure} hPa\n"
                       f"Precipitation: {precipitation} %")

        lbl_result.config(text=result_text)
    else:
        messagebox.showerror("Error", "Failed to retrieve weather data.")


window = tk.Tk()
window.title("Weather Information")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_location = tk.Entry(master=frm_entry, width=20)
lbl_location = tk.Label(master=frm_entry, text="Location:")

ent_location.grid(row=0, column=1, sticky="w")
lbl_location.grid(row=0, column=0, sticky="e")

btn_search = tk.Button(master=window, text="Search", command=search_weather)
lbl_result = tk.Label(master=window, text="", justify=tk.LEFT)

frm_entry.grid(row=0, column=0, padx=10)
btn_search.grid(row=0, column=1, pady=10)
lbl_result.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()

