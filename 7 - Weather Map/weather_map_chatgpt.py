import requests
import tkinter as tk
from tkinter import messagebox

# Constants
API_KEY = '97794765406e651526df5bbf886d903f'
BASE_URL = 'https://api.openweathermap.org/data/3.0/onecall?'

# Function to get weather data for a specified location
def get_weather_data(lat, lon):
    try:
        complete_url = f"{BASE_URL}lat={lat}&lon={lon}&appid={API_KEY}"
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return None

# Function to display the weather data for the specified location
def get_weather():
    location = ent_location.get()
    if location.lower() == "london":
        lat, lon = 51.507351, -0.127758
    else:
        messagebox.showerror("Error", "Location not supported.")
        return

    weather_data = get_weather_data(lat, lon)
    if weather_data:
        temp = weather_data['current']['temp'] - 273.15
        humidity = weather_data['current']['humidity']
        wind_speed = weather_data['current']['wind_speed']
        pressure = weather_data['current']['pressure']
        precipitation = weather_data.get('daily', [{}])[0].get('rain', 0)

        result_text = (f"Temperature: {temp:.2f}°C\n"
                       f"Humidity: {humidity}%\n"
                       f"Wind Speed: {wind_speed} m/s\n"
                       f"Pressure: {pressure} hPa\n"
                       f"Precipitation: {precipitation} %")

        lbl_result.config(text=result_text)
    else:
        messagebox.showerror("Error", "Failed to retrieve weather data.")


# Tkinter GUI setup
window = tk.Tk()
window.title("Weather Information")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_location = tk.Entry(master=frm_entry, width=20)
lbl_location = tk.Label(master=frm_entry, text="Location:")

ent_location.grid(row=0, column=1, sticky="w")
lbl_location.grid(row=0, column=0, sticky="e")

btn_search = tk.Button(master=window, text="Search", command=get_weather)
lbl_result = tk.Label(master=window, text="", justify=tk.LEFT)

frm_entry.grid(row=0, column=0, padx=10)
btn_search.grid(row=0, column=1, pady=10)
lbl_result.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

window.geometry("350x250")
window.mainloop()
