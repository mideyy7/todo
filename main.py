import tkinter as tk

root = tk.Tk()

tasks = []

def toggle_task(task_info):
    task_label = task_info['label']
    if task_info['done']:
        task_label.config(fg = 'black', font = ('TkDefaultFont', 10, 'normal'))
        task_info['done'] = False
    else:
        task_label.config(fg = 'grey', font = ('TkDefaultFont', 10, 'normal'))
        task_info['done'] = True


def add_task(event = None):
    task = entry.get().strip()
    if task:
        tasks.append(task)
 
        task_label = tk.Label(task_frame, text = task, anchor = 'w')  #by default text in a label is centerd. anchor makes it aligned to the left
        task_label.pack(fill = 'x', pady = 2)  #fill asllows it to use all the available space

        task_info = {
            'label': task_label,
            'done': False
        }

        task_label.bind("<Button-1>", lambda event : toggle_task(task_info))

        entry.delete(0, tk.END)


    else:
        print("Empty task: Nothing was added")
        return

    print("Task has been successfully added to the list")

root.title("Simple Task List ")
root.geometry("300x300+200+200")    #300 X 300 : WIDTH X HEIGHT . 200 MARGIN TO THE LEFT AND 200 MARGIN TO THE TOP

input_frame = tk.Frame(root)
task_frame = tk.Frame(root)

input_frame.pack()
task_frame.pack(padx = 10, fill = 'x')

entry = tk.Entry(input_frame, width=35)
button = tk.Button(input_frame, text="Add Task: ", command=add_task)
entry.focus()  

entry.grid(row = 0, column = 0)
button.grid(row = 0, column = 1, padx = 5)

entry.bind("<Return>", add_task)


root.mainloop()