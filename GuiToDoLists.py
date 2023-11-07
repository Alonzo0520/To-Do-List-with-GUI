import tkinter as tk

# Initialize an empty list to store tasks
tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        listbox.delete(index)
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task['task']}' removed.")

def mark_task_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task = tasks[index]
        if not task["completed"]:
            task["completed"] = True
            listbox.itemconfig(index, {'bg': 'green'})
        else:
            print(f"Task '{task['task']}' is already completed.")

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Entry for adding tasks
entry = tk.Entry(root, width=40)
entry.pack()

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=60, height=20)
listbox.pack()

# Remove task button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Mark as completed button
complete_button = tk.Button(root, text="Mark as Completed", command=mark_task_completed)
complete_button.pack()

# Start the GUI main loop
root.mainloop()
