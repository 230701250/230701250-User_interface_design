import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Task Manager")

        self.tasks = []

        
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        
        self.add_button = tk.Button(root, text="Add Task", width=20, command=self.add_task)
        self.add_button.pack()

    
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

    
        self.remove_button = tk.Button(root, text="Remove Selected Task", width=20, command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            removed = self.tasks.pop(index)
            self.update_task_list()
            messagebox.showinfo("Task Removed", f"Removed: {removed}")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{idx}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
