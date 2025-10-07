import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

# ------------------- FILE SETUP -------------------
DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

# ------------------- THEME COLORS -------------------
THEMES = {
    "light": {
        "bg": "#F5F5F0",
        "card": "#ffffff",
        "text": "#000000",
        "completed": "#d5f5d5"
    },
    "dark": {
        "bg": "#2b2b2b",
        "card": "#3a3a3a",
        "text": "#ffffff",
        "completed": "#335533"
    }
}
current_theme = "light"

# ------------------- MAIN LOGIC -------------------
def add_task():
    title = task_entry.get().strip()
    due = due_entry.get().strip()
    priority = priority_combo.get()

    if not title:
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    task = {
        "title": title,
        "due": due,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    save_tasks()
    task_entry.delete(0, tk.END)
    due_entry.delete(0, tk.END)
    render_tasks()

def delete_task(index):
    del tasks[index]
    save_tasks()
    render_tasks()

def delete_all_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?"):
        tasks.clear()
        save_tasks()
        render_tasks()

def complete_task(index):
    tasks[index]["completed"] = not tasks[index]["completed"]
    save_tasks()
    render_tasks()

def sort_tasks():
    option = sort_combo.get()
    if option == "Due Date":
        tasks.sort(key=lambda x: datetime.strptime(x["due"], "%Y-%m-%d") if x["due"] else datetime.max)
    elif option == "Priority":
        order = {"High": 1, "Medium": 2, "Low": 3}
        tasks.sort(key=lambda x: order.get(x["priority"], 4))
    save_tasks()
    render_tasks()

def search_tasks(*args):
    query = search_var.get().lower()
    render_tasks(query)

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    theme = THEMES[current_theme]
    root.configure(bg=theme["bg"])
    search_frame.configure(bg=theme["bg"])
    input_frame.config(bg=theme["bg"])
    task_frame.configure(bg=theme["bg"])
    bottom_frame.configure(bg=theme["bg"])
    render_tasks()

def apply_theme():
    theme = THEMES[current_theme]
    root.config(bg=theme["bg"])
    input_frame.config(bg=theme["bg"])
    search_frame.config(bg=theme["bg"])
    task_frame.config(bg=theme["bg"])
    render_tasks()

# ------------------- UI SETUP -------------------
root = tk.Tk()
root.title("🗂️ Task Tracker")
root.geometry("800x650")
root.config(bg=THEMES[current_theme]["bg"])

style = ttk.Style()
style.theme_use("clam")

# Hover effect
def on_enter(e):
    e.widget['background'] = '#d1d1e0'
def on_leave(e):
    e.widget['background'] = '#e6e6fa'

style.configure("TButton",
                font=("Segoe UI", 10, "bold"),
                background="#e6e6fa",
                foreground="#333",
                borderwidth=1,
                relief="flat")
style.map("TButton", background=[("active", "#d1d1e0")])

# ------------------- INPUT AREA -------------------
input_frame = tk.Frame(root, bg=THEMES[current_theme]["bg"])
input_frame.pack(pady=15)

tk.Label(input_frame, text="Task:", bg=THEMES[current_theme]["bg"], font=("Segoe UI", 11)).grid(row=0, column=0, padx=5)
task_entry = tk.Entry(input_frame, width=25, font=("Segoe UI", 11))
task_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Due Date (YYYY-MM-DD):", bg=THEMES[current_theme]["bg"], font=("Segoe UI", 11)).grid(row=0, column=2, padx=5)
due_entry = tk.Entry(input_frame, width=12, font=("Segoe UI", 11))
due_entry.grid(row=0, column=3, padx=5)

tk.Label(input_frame, text="Priority:", bg=THEMES[current_theme]["bg"], font=("Segoe UI", 11)).grid(row=0, column=4, padx=5)
priority_combo = ttk.Combobox(input_frame, values=["Low", "Medium", "High"], width=8, font=("Segoe UI", 10))
priority_combo.grid(row=0, column=5, padx=5)
priority_combo.current(1)

add_btn = tk.Button(input_frame, text="Add Task", font=("Segoe UI", 10, "bold"),
                    bg="#e6e6fa", relief="flat", command=add_task)
add_btn.grid(row=0, column=6, padx=10)
add_btn.bind("<Enter>", on_enter)
add_btn.bind("<Leave>", on_leave)

# ------------------- SEARCH + SORT + THEME -------------------
search_frame = tk.Frame(root, bg=THEMES[current_theme]["bg"])
search_frame.pack(pady=5)

search_var = tk.StringVar()
search_var.trace("w", search_tasks)
search_entry = tk.Entry(search_frame, textvariable=search_var, width=30, font=("Segoe UI", 11))
search_entry.grid(row=0, column=0, padx=5)
search_entry.insert(0, "🔍 Search tasks...")

sort_combo = ttk.Combobox(search_frame, values=["None", "Due Date", "Priority"], width=12, font=("Segoe UI", 10))
sort_combo.grid(row=0, column=1, padx=5)
sort_combo.current(0)

sort_btn = tk.Button(search_frame, text="Sort", command=sort_tasks, bg="#e6e6fa", relief="flat")
sort_btn.grid(row=0, column=2, padx=5)
sort_btn.bind("<Enter>", on_enter)
sort_btn.bind("<Leave>", on_leave)

theme_btn = tk.Button(search_frame, text="🌓 Toggle Theme", command=toggle_theme, bg="#e6e6fa", relief="flat")
theme_btn.grid(row=0, column=3, padx=5)
theme_btn.bind("<Enter>", on_enter)
theme_btn.bind("<Leave>", on_leave)

# ------------------- TASK DISPLAY -------------------
task_frame = tk.Frame(root, bg=THEMES[current_theme]["bg"])
task_frame.pack(pady=10, fill="both", expand=True)

def render_tasks(query=""):
    theme = THEMES[current_theme]
    for widget in task_frame.winfo_children():
        widget.destroy()

    filtered = [t for t in tasks if query.lower() in t["title"].lower()]

    if not filtered:
        tk.Label(task_frame, text="No tasks found!", font=("Segoe UI", 12), bg=theme["bg"], fg=theme["text"]).pack(pady=20)
        return

    for i, task in enumerate(filtered):
        color = theme["completed"] if task["completed"] else theme["card"]
        card = tk.Frame(task_frame, bg=color, relief="groove", bd=2)
        card.pack(pady=6, padx=20, fill="x")

        card.columnconfigure(0, weight=0)
        card.columnconfigure(1, weight=1)
        card.columnconfigure(2, weight=0)

        title_lbl = tk.Label(card, text=task["title"], font=("Segoe UI", 11, "bold"),
                         bg=color, fg=theme["text"], anchor="w")
        title_lbl.grid(row=0, column=0, sticky="w", padx=10, pady=3)

        due_lbl = tk.Label(card, text=f"Due: {task['due'] or 'N/A'}", font=("Segoe UI", 9),
                       bg=color, fg=theme["text"])
        due_lbl.grid(row=1, column=0, sticky="w", padx=10)

        pri_lbl = tk.Label(card, text=f"Priority: {task['priority']}", font=("Segoe UI", 9),
                       bg=color, fg=theme["text"])
        pri_lbl.grid(row=1, column=1, sticky="w", padx=10)

        btn_frame = tk.Frame(card, bg=color)
        btn_frame.grid(row=0, column=2, rowspan=2, sticky="e", padx=10)

        delete_btn = tk.Button(btn_frame, text="🗑", font=("Segoe UI", 10, "bold"),
                           bg="#ffcccc", command=lambda i=i: delete_task(tasks.index(filtered[i])))
        delete_btn.pack(side="right", padx=5)

        complete_btn = tk.Button(btn_frame, text="✓", font=("Segoe UI", 10, "bold"),
                             bg="#ccffcc", command=lambda i=i: complete_task(tasks.index(filtered[i])))
        complete_btn.pack(side="right", padx=5)
        
# ------------------- BOTTOM BUTTON AREA -------------------
bottom_frame = tk.Frame(root, bg=THEMES[current_theme]["bg"])
bottom_frame.pack(fill="x", pady=10, padx=20, anchor="se")

delete_all_btn = tk.Button(bottom_frame, text="Delete All", command=delete_all_tasks,
                           font=("Segoe UI", 10, "bold"),
                           bg="#ffcccc", relief="flat", padx=10, pady=5)
delete_all_btn.pack(side="right", anchor="se")

delete_all_btn.bind("<Enter>", on_enter)
delete_all_btn.bind("<Leave>", on_leave)


render_tasks()
root.mainloop()
