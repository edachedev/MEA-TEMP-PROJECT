import tkinter as tk
from tkinter import Label, Entry, Button, Radiobutton

def convert_temperature():
    try:
        temperature = float(entry.get())
        unit = unit_var.get()

        if unit == "Celsius":
            converted_temperature = (temperature * 9/5) + 32
            result_label.config(text=f"Converted Temperature: {converted_temperature:.2f} °F")
        elif unit == "Fahrenheit":
            converted_temperature = (temperature - 32) * 5/9
            result_label.config(text=f"Converted Temperature: {converted_temperature:.2f} °C")
    except ValueError:
        result_label.config(text="Please enter a valid temperature.")

