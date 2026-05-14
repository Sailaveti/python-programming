import tkinter as tk

# Function for button click
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# Function to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear screen
def clear():
    entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x400")
root.config(bg="lightblue")

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=5, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Button frame
frame = tk.Frame(root)
frame.pack()

# Buttons
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create buttons
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            b = tk.Button(row_frame, text=btn, font=("Arial", 18),
                          command=calculate, height=2, width=5)
        else:
            b = tk.Button(row_frame, text=btn, font=("Arial", 18),
                          command=lambda x=btn: click(x), height=2, width=5)

        b.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 18),
                      command=clear, bg="red", fg="white")
clear_btn.pack(fill="both", padx=10, pady=10)

# Run app
root.mainloop()