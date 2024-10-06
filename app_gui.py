import requests
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext, messagebox, PhotoImage

# Function to fetch asteroid data
def fetch_asteroid_data():
    API_KEY = "FmR2fL8mNtwGhHhgkCUUszdDVQRq9XT9VPHY2adm"
    
    today = datetime.today().strftime('%Y-%m-%d')
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={today}&api_key={API_KEY}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        output_text.delete(1.0, tk.END)  # Clear previous output
        
        if today in data['near_earth_objects']:
            for obj in data['near_earth_objects'][today]:
                name = obj['name']
                distance = float(obj['close_approach_data'][0]['miss_distance']['kilometers'])
                velocity = float(obj['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
                hazardous = obj['is_potentially_hazardous_asteroid']

                output_text.insert(tk.END, f"Asteroid: {name}\n")
                output_text.insert(tk.END, f"Closest Distance: {distance:.2f} km\n")
                output_text.insert(tk.END, f"Speed: {velocity:.2f} km/h\n")
                output_text.insert(tk.END, f"Potentially Hazardous: {'Yes' if hazardous else 'No'}\n")
                output_text.insert(tk.END, "-------------\n")
        else:
            output_text.insert(tk.END, "No near-Earth objects found for today.\n")
    else:
        messagebox.showerror("Error", f"Failed to fetch data from NASA API. Status code: {response.status_code}")

# Create the main application window
app = tk.Tk()
app.title("Asteroid Tracker")
app.geometry("500x500")
app.configure(bg="#282c34")  # Background color

# Add a title label
title_label = tk.Label(app, text="Near-Earth Asteroid Tracker", font=("Helvetica", 16), fg="#61dafb", bg="#282c34")
title_label.pack(pady=10)

# Create a button to fetch asteroid data
fetch_button = tk.Button(app, text="Fetch Asteroid Data", command=fetch_asteroid_data, font=("Helvetica", 12), bg="#61dafb", fg="white")
fetch_button.pack(pady=10)

# Create a scrolled text area to display output
output_text = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=60, height=20, font=("Helvetica", 10), bg="#f6f8fa", fg="#282c34")
output_text.pack(pady=10)

# Add a footer label
footer_label = tk.Label(app, text="Data provided by NASA API", font=("Helvetica", 10), fg="white", bg="#282c34")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Start the GUI event loop
app.mainloop()
