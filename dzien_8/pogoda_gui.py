# pip install pyinstaller
# pyinstaller --onefile --noconsole pogoda_gui.py

import tkinter
from pogoda import get_location_id, get_location_weather

def weather_report():
    location_id =get_location_id(location_entry.get())
    weather = get_location_weather(location_id)
    report.configure(text=weather.raport())

root = tkinter.Tk()
location_entry = tkinter.Entry(root)
submit = tkinter.Button(root, text="Pobierz", command=weather_report)
report = tkinter.Label(root, text="-")

location_entry.grid(row=1, column=1)
submit.grid(row=1, column=2)
report.grid(row=1, column=3)
root.mainloop()