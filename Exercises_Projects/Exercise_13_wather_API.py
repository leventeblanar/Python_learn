from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox 
from timezonefinder import TimezoneFinder
from datetime import datetime 
import requests
import pytz

root=Tk()
root.title("Wather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


#search box
Search_image = PhotoImage(file="Exercises_Projects/search.png")
myimage=Label(image=Search_image)
myimage.place(x=20, y=20)

textfield=tk.Entry(root,justify="center",width=17, font=("poppins", 25, "bold"))
textfield.place(x=60,y=45)
textfield.focus()

root.mainloop()
