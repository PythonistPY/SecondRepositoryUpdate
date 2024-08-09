import tkinter as tk
from tkinter import messagebox

def delete_task():
    selected_task = task_list_box.curselection()
    if selected_task:
        if messagebox.askyesno("Подтверждение удаления", "Вы уверены, что хотите удалить выбранную задачу?"):
            task_list_box.delete(selected_task)

def add_task():
    task = task_entry.get()
    if task:
        task_list_box.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def mark_task():
    selected_task = task_list_box.curselection()
    if selected_task:
        task_list_box.itemconfig(selected_task, {'bg': 'light green'})
        task_list_box.selection_clear(selected_task)

def unmark_task():
    selected_task = task_list_box.curselection()
    if selected_task:
        task_list_box.itemconfig(selected_task, {'bg': 'DarkSlateGrey'})
        task_list_box.selection_clear(selected_task)

root = tk.Tk()
root.title("Personal NOTEBOOK")
root.geometry('600x480')
root["bg"] = 'black'

text1 = tk.Label(root, text="Введите свою задачу ", bg="DarkSlateGrey", font=("Arial Bold", 15))
text1.pack(pady=10)

task_entry = tk.Entry(root, width=30, bg="DarkSlateGrey")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить Задачу", command=add_task, bg="chartreuse4")
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", command=delete_task, bg="brown4")
delete_button.pack(pady=5)

confirm_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task, bg="chartreuse4")
confirm_button.pack(pady=5)

unmark_button = tk.Button(root, text="Снять отметку с задачи", command=unmark_task, bg="orange")
unmark_button.pack(pady=5)

text2 = tk.Label(root, text="Список Задач!", bg="dark green")
text2.pack(pady=10)

task_list_box = tk.Listbox(root, height=10, width=50, bg="DarkSlateGrey", selectmode=tk.SINGLE)
task_list_box.pack(pady=20)

root.mainloop()
