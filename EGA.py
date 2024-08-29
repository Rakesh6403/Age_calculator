import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    name = name_entry.get()
    dob = dob_entry.get()

    try:
        birth_date = datetime.strptime(dob, "%d/%m/%Y")
        today = datetime.today()

        # Check if the entered date is in the future
        if birth_date > today:
            messagebox.showerror("Invalid Date", "The date of birth cannot be in the future.")
            return

        # Calculate the difference in years, months, and days
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        # Adjust if necessary
        if days < 0:
            months -= 1
            days += (birth_date.replace(year=today.year, month=birth_date.month + 1, day=1) - birth_date.replace(year=today.year, month=birth_date.month, day=1)).days

        if months < 0:
            years -= 1
            months += 12

        messagebox.showinfo("Age Calculator", f"Hello {name}, your age is {years} years, {months} months, and {days} days.")
    except ValueError:
        messagebox.showerror("Invalid Date Format", "Please enter the date in DD/MM/YYYY format.")


def create_gradient(canvas, width, height, color1, color2):
    """ Create a gradient background on a Canvas. """
    for i in range(height):
        ratio = i / height
        red = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        green = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        blue = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        color = f'#{red:02x}{green:02x}{blue:02x}'
        canvas.create_line(0, i, width, i, fill=color)

        # Store the gradient colors to set widget background
        if i in [75, 125, 175]:  # approximate y-coordinates where widgets will be placed
            gradient_colors[i] = color

# Creating the main window
root = tk.Tk()
root.title("Age Calculator")
root.geometry("600x250")
root.resizable(False, False)  # Disable window resizing

# Create a Canvas widget for the gradient background
canvas = tk.Canvas(root, width=600, height=250, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Define gradient colors (color1 and color2 are RGB tuples)
color1 = (255, 123, 67)  # Orange
color2 = (61, 90, 241)   # Blue

gradient_colors = {}
create_gradient(canvas, 600, 250, color1, color2)

# Adding styled widgets directly to the canvas
label_name = tk.Label(root, text="Name:", font=("Helvetica", 12), bg=gradient_colors[75], fg="black")
canvas.create_window(150, 75, window=label_name, anchor='w')

name_entry = tk.Entry(root, font=("Helvetica", 12), bd=2, relief="solid", bg=gradient_colors[75])
canvas.create_window(300, 75, window=name_entry, anchor='w')

label_dob = tk.Label(root, text="Date of Birth\n(DD/MM/YYYY):", font=("Helvetica", 12), bg=gradient_colors[125], fg="black")
canvas.create_window(120, 125, window=label_dob, anchor='w')

dob_entry = tk.Entry(root, font=("Helvetica", 12), bd=2, relief="solid", bg=gradient_colors[125])
canvas.create_window(300, 125, window=dob_entry, anchor='w')

button = tk.Button(root, text="OK", command=calculate_age, font=("Helvetica", 12, "bold"), bg=gradient_colors[175], fg="black", bd=2, relief="raised")
canvas.create_window(300, 175, window=button, anchor='center')

# Running the main event loop
root.mainloop()
