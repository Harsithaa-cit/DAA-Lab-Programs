import tkinter as tk
from tkinter import ttk, messagebox
import time

# ------------------------------------------
# Student Details (Sorted by Roll Number)
# ------------------------------------------
students = [
    (101, "Arun"),
    (105, "Priya"),
    (108, "Rahul"),
    (112, "Sneha"),
    (118, "Kavin"),
    (120, "Anitha"),
    (125, "Vijay"),
    (130, "Divya"),
    (135, "Ajay"),
    (140, "Meena"),
    (145, "Harish"),
    (150, "Nisha"),
    (155, "Surya"),
    (160, "Keerthi"),
    (165, "Manoj"),
    (170, "Deepika"),
    (175, "Karthik"),
    (180, "Pooja"),
    (185, "Ramesh"),
    (190, "Aarthi")
]

roll_numbers = [student[0] for student in students]


# ------------------------------------------
# Interpolation Search
# ------------------------------------------
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:

        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


# ------------------------------------------
# Search Function
# ------------------------------------------
def search_student():

    try:
        target = int(entry_roll.get())

    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid Roll Number.")
        return

    start = time.perf_counter()

    index, comparisons = interpolation_search(roll_numbers, target)

    end = time.perf_counter()

    execution_time = (end - start) * 1000

    if index != -1:

        roll, name = students[index]

        result.config(
            text=f"""Student Found

Name            : {name}
Roll Number     : {roll}
Position        : {index + 1}
Comparisons     : {comparisons}
Execution Time  : {execution_time:.6f} ms
""",
            fg="green"
        )

        messagebox.showinfo(
            "Search Successful",
            f"{name} (Roll No: {roll}) Found Successfully!"
        )

    else:

        result.config(
            text="Roll Number Not Found!",
            fg="red"
        )

        messagebox.showerror(
            "Search Failed",
            "Roll Number does not exist."
        )


# ------------------------------------------
# Clear Function
# ------------------------------------------
def clear_fields():
    entry_roll.delete(0, tk.END)
    result.config(text="")


# ------------------------------------------
# GUI
# ------------------------------------------

root = tk.Tk()
root.title("Student Roll Number Search System")
root.geometry("900x650")
root.configure(bg="#EAF4FC")
root.resizable(False, False)

title = tk.Label(
    root,
    text="STUDENT ROLL NUMBER SEARCH SYSTEM",
    bg="#0A4D8C",
    fg="white",
    font=("Segoe UI", 20, "bold"),
    pady=10
)
title.pack(fill="x")

college = tk.Label(
    root,
    text="Chennai Institute of Technology",
    bg="#EAF4FC",
    fg="#0A4D8C",
    font=("Segoe UI", 15, "bold")
)
college.pack(pady=(15,0))

department = tk.Label(
    root,
    text="Department : CSE (Artificial Intelligence and Machine Learning)",
    bg="#EAF4FC",
    fg="#0A4D8C",
    font=("Segoe UI", 11, "bold")
)
department.pack()

algorithm = tk.Label(
    root,
    text="Algorithm Used : Interpolation Search",
    bg="#EAF4FC",
    fg="gray30",
    font=("Segoe UI", 11)
)
algorithm.pack(pady=(0,15))

columns = ("Roll Number", "Student Name")

tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

tree.heading("Roll Number", text="Roll Number")
tree.heading("Student Name", text="Student Name")

tree.column("Roll Number", width=180, anchor="center")
tree.column("Student Name", width=250, anchor="center")

for roll, name in students:
    tree.insert("", tk.END, values=(roll, name))

tree.pack()

frame = tk.Frame(root, bg="#EAF4FC")
frame.pack(pady=20)

tk.Label(
    frame,
    text="Enter Roll Number",
    bg="#EAF4FC",
    font=("Segoe UI", 12, "bold")
).grid(row=0, column=0, padx=10)

entry_roll = tk.Entry(
    frame,
    font=("Segoe UI", 13),
    width=18,
    justify="center"
)
entry_roll.grid(row=0, column=1)

button_frame = tk.Frame(root, bg="#EAF4FC")
button_frame.pack(pady=15)

search_btn = tk.Button(
    button_frame,
    text="🔍 Search",
    bg="#0078D7",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15,
    command=search_student
)
search_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    button_frame,
    text="🧹 Clear",
    bg="#F39C12",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15,
    command=clear_fields
)
clear_btn.grid(row=0, column=1, padx=10)

exit_btn = tk.Button(
    button_frame,
    text="🚪 Exit",
    bg="#D9534F",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=15,
    command=root.destroy
)
exit_btn.grid(row=0, column=2, padx=10)

result = tk.Label(
    root,
    text="",
    bg="#EAF4FC",
    justify="left",
    font=("Consolas", 12, "bold")
)
result.pack(pady=20)

footer = tk.Label(
    root,
    text="Design and Analysis of Algorithms Mini Project",
    bg="#0A4D8C",
    fg="white",
    font=("Segoe UI", 10)
)
footer.pack(side="bottom", fill="x")

root.mainloop()