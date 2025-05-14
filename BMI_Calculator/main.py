# main.py

import tkinter as tk
from tkinter import messagebox
from bmi_utils import calculate_bmi, get_bmi_category
from data_handler import save_bmi_record, load_user_data
from bmi_plotter import plot_bmi_history

def calculate_and_show_bmi():
    try:
        name = name_entry.get().strip()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if not name:
            raise ValueError("Name is required.")
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
        save_bmi_record(name, bmi)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def show_history():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Missing Name", "Please enter a name first.")
        return

    records = load_user_data(name)
    if not records:
        messagebox.showinfo("No Data", "No BMI data found for this user.")
        return

    dates, bmis = zip(*records)
    plot_bmi_history(dates, bmis, name)

# GUI Setup
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("300x350")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_and_show_bmi).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

tk.Button(root, text="Show BMI History", command=show_history).pack(pady=10)

root.mainloop()
