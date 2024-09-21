import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import pytz

timezones = ["IST", "UTC", "EST", "CST", "PST"]

def convert_time():
    try:
        input_time_str = time_entry.get()  # Input time in HH:MM format (no seconds)
        am_pm = am_pm_combobox.get()  # AM or PM
        from_zone_str = from_zone_combobox.get()
        to_zone_str = to_zone_combobox.get()

        selected_day = day_combobox.get()
        selected_month = month_combobox.get()
        selected_year = year_combobox.get()
        
        selected_date_str = f"{selected_year}-{selected_month}-{selected_day}"

        time_format = "%I:%M %p"
        full_input_time_str = f"{input_time_str} {am_pm}"
        input_time = datetime.strptime(full_input_time_str, time_format)

        input_time_str_with_date = f"{selected_date_str} {input_time.strftime('%H:%M')}"
        input_time_with_date = datetime.strptime(input_time_str_with_date, "%Y-%m-%d %H:%M")

        timezone_map = {
            "IST": pytz.timezone("Asia/Kolkata"),
            "UTC": pytz.utc,
            "EST": pytz.timezone("US/Eastern"),
            "CST": pytz.timezone("US/Central"),
            "PST": pytz.timezone("US/Pacific")
        }

        from_zone = timezone_map[from_zone_str]
        to_zone = timezone_map[to_zone_str]

        input_time_with_date = from_zone.localize(input_time_with_date)

        target_time = input_time_with_date.astimezone(to_zone)
        result_label.config(text=f"Converted Time: {target_time.strftime('%Y-%m-%d %I:%M %p')}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Time Zone Converter")

time_label = tk.Label(root, text="Enter Time (HH:MM):")
time_label.grid(row=0, column=0, padx=10, pady=10)
time_entry = tk.Entry(root)
time_entry.grid(row=0, column=1, padx=10, pady=10)

am_pm_label = tk.Label(root, text="AM/PM:")
am_pm_label.grid(row=1, column=0, padx=10, pady=10)
am_pm_combobox = ttk.Combobox(root, values=["AM", "PM"])
am_pm_combobox.grid(row=1, column=1, padx=10, pady=10)
am_pm_combobox.current(0)  # Default to AM

from_zone_label = tk.Label(root, text="From Timezone:")
from_zone_label.grid(row=2, column=0, padx=10, pady=10)
from_zone_combobox = ttk.Combobox(root, values=timezones)
from_zone_combobox.grid(row=2, column=1, padx=10, pady=10)
from_zone_combobox.current(0)  # Default to IST

to_zone_label = tk.Label(root, text="To Timezone:")
to_zone_label.grid(row=3, column=0, padx=10, pady=10)
to_zone_combobox = ttk.Combobox(root, values=timezones)
to_zone_combobox.grid(row=3, column=1, padx=10, pady=10)
to_zone_combobox.current(1)  # Default to UTC

day_label = tk.Label(root, text="Day:")
day_label.grid(row=4, column=0, padx=10, pady=10)
day_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 32)])  # Days 01-31
day_combobox.grid(row=4, column=1, padx=10, pady=10)
day_combobox.current(0)

month_label = tk.Label(root, text="Month:")
month_label.grid(row=5, column=0, padx=10, pady=10)
month_combobox = ttk.Combobox(root, values=[str(i).zfill(2) for i in range(1, 13)])  # Months 01-12
month_combobox.grid(row=5, column=1, padx=10, pady=10)
month_combobox.current(0)

year_label = tk.Label(root, text="Year:")
year_label.grid(row=6, column=0, padx=10, pady=10)
year_combobox = ttk.Combobox(root, values=[str(i) for i in range(2020, 2031)])  # Years 2020-2030
year_combobox.grid(row=6, column=1, padx=10, pady=10)
year_combobox.current(4)  # Default to the current year (2024)

convert_button = tk.Button(root, text="Convert", command=convert_time)
convert_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Converted Time: ")
result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
