from weather_module import get_weather
import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title("Weather App")
window.geometry("400x500")

# Create a label
label = ttk.Label(window, text="Weather App")
label.config(font=("Arial", 30))
label.pack()

# Create a text field
city = tk.StringVar()
city_entry = ttk.Entry(window, textvariable=city)
city_entry.pack()


# Create a button
def button_pressed():
    city_name = city.get()
    weather = get_weather(city_name)
    results.set(weather)


button = ttk.Button(window, text="Get Weather", command=button_pressed)
button.pack()

# Show the result in a label
results = tk.StringVar()
result_label = ttk.Label(window, textvariable=results)
result_label.pack()

tk.mainloop()
