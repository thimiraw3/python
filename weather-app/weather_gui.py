import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io

# OpenWeatherMap API Key
API_KEY = "YOUR_API_KEY"  # <-- Replace with your key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

recent_cities = []

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    units = "metric" if unit_var.get() == "C" else "imperial"
    unit_symbol = "°C" if unit_var.get() == "C" else "°F"

    url = BASE_URL + f"appid={API_KEY}&q={city}&units={units}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']

        temp = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        pressure = main['pressure']
        condition = weather['description'].capitalize()
        wind_speed = wind['speed']

        # icon
        icon_code = weather['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        if icon_response.status_code == 200:
            img_data = icon_response.content
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((100, 100))
            tk_img = ImageTk.PhotoImage(img)
            weather_icon_label.config(image=tk_img)
            weather_icon_label.image = tk_img

        # boxes
        temp_label.config(text=f"{temp}{unit_symbol}")
        feels_label.config(text=f"{feels_like}{unit_symbol}")
        humidity_label.config(text=f"{humidity}%")
        pressure_label.config(text=f"{pressure} hPa")
        wind_label.config(text=f"{wind_speed} m/s")
        condition_label.config(text=condition)

        # Save to history
        if city not in recent_cities:
            recent_cities.append(city)
            history_combo['values'] = recent_cities
    else:
        messagebox.showerror("Error", "City not found!")

def load_from_history(event):
    selected_city = history_combo.get()
    city_entry.delete(0, tk.END)
    city_entry.insert(0, selected_city)
    get_weather()


root = tk.Tk()
root.title("🌦 Weather App")
root.geometry("600x650")
root.resizable(False, False)
root.configure(bg="#FFFFFF")

title_label = tk.Label(root, text="🌤 Weather App", font=("Arial", 20, "bold"), bg="#FFFFFF", fg="#003366")
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), justify="center", width=25, bg="#D9D9D9")
city_entry.pack(pady=10)

unit_var = tk.StringVar(value="C")
unit_frame = tk.Frame(root, bg="#FFFFFF")
unit_frame.pack(pady=5)
tk.Label(unit_frame, text="Units:", font=("Arial", 12), bg="#FFFFFF").pack(side="left", padx=5)
tk.Radiobutton(unit_frame, text="Celsius (°C)", variable=unit_var, value="C", bg="#FFFFFF").pack(side="left")
tk.Radiobutton(unit_frame, text="Fahrenheit (°F)", variable=unit_var, value="F", bg="#FFFFFF").pack(side="left")

search_button = tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"),
                          bg="#4682b4", fg="white", width=15, command=get_weather)
search_button.pack(pady=10)

weather_icon_label = tk.Label(root, bg="#FFFFFF")
weather_icon_label.pack(pady=10)

frame = tk.Frame(root, bg="#FFFFFF")
frame.pack(pady=20)

def create_box(parent, title, row, col):
    box = tk.Frame(parent, bg="white", relief="solid", bd=1, padx=20, pady=15)
    box.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")  # place in grid
    tk.Label(box, text=title, font=("Arial", 12, "bold"), bg="white").pack()
    value_label = tk.Label(box, text="--", font=("Arial", 14), bg="white")
    value_label.pack()
    return value_label

temp_label = create_box(frame, "🌡 Temperature",0,0)
feels_label = create_box(frame, "🤔 Feels Like",0,1)
humidity_label = create_box(frame, "💧 Humidity",0,2)
    
pressure_label = create_box(frame, "⏲ Pressure",1,0)
wind_label = create_box(frame, "🍃 Wind Speed",1,1)
condition_label = create_box(frame, "☁️ Condition",1,2)

tk.Label(root, text="Recent Searches:", font=("Arial", 12, "bold"), bg="#FFFFFF").pack()
history_combo = ttk.Combobox(root, state="readonly")
history_combo.pack(pady=5)
history_combo.bind("<<ComboboxSelected>>", load_from_history)

root.mainloop()
