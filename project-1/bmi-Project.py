import tkinter as tk
from tkinter import messagebox

# ---------------------- BMI FUNCTION ----------------------
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height_cm = float(entry_height.get())

        if weight <= 0 or height_cm <= 0:
            raise ValueError

        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        category = get_category(bmi)

        result_label.config(text=f"BMI: {bmi} ({category})")

    except ValueError:
        messagebox.showerror("Error", "Enter valid positive numbers!")


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# ---------------------- GUI ----------------------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")

# Labels & Inputs
tk.Label(root, text="Weight (kg)").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (cm)").pack()
entry_height = tk.Entry(root)
entry_height.pack()

# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result
result_label = tk.Label(root, text="Your BMI will appear here")
result_label.pack(pady=20)

root.mainloop()