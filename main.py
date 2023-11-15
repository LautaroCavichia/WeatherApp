from weather_module import get_weather
from cities_module import get_city_suggestions
import tkinter as tk
from tkinter import ttk


def on_city_change(*args):
    city_name = city_var.get()
    suggestions = get_city_suggestions(city_name)
    city_combobox['values'] = suggestions


window = tk.Tk()
window.title("Weather App")
window.geometry("400x500")

label = ttk.Label(window, text="Weather App")
label.config(font=("Arial", 30))
label.pack()

# Create a Combobox for city entry with autocomplete
city_var = tk.StringVar()
city_var.trace_add('write', on_city_change)  # Call on_city_change when the variable changes
city_combobox = ttk.Combobox(window, textvariable=city_var)
city_combobox.pack()


def button_pressed():
    city_name = city_var.get()
    weather = get_weather(city_name)
    results.set(weather)


button = ttk.Button(window, text="Get Weather", command=button_pressed)
button.pack()

results = tk.StringVar()
result_label = ttk.Label(window, textvariable=results)
result_label.pack()

tk.mainloop()
