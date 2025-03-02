# Program: tkinter Practice
# Author: Zachariah King
# Date: 3/2/25
# Description: This algorithm uses the tkinter module to create a GUI application
#              that acts as a customizable To Do list with distinct color schemes
#              and the ability to add items, delete items, and exit the program
#              entirely.

import tkinter as tk
import tkinter.messagebox as msg

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()
        
        self.create_menu()
        
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks
            
        self.tasks_canvas = tk.Canvas(self)
        
        self.tasks_frame = tk.Frame(self.tasks_canvas)
        self.text_frame = tk.Frame(self)
        
        self.scrollbar = tk.Scrollbar(self.tasks_canvas, orient="vertical", command=self.tasks_canvas.yview)
        
        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.title("King-ToDo") # Changed the title of the window
        self.geometry("300x400")
        
        self.task_create = tk.Text(self.text_frame, height=3, bg="white", fg="black")
        
        self.tasks_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas_frame = self.tasks_canvas.create_window((0,0), window=self.tasks_frame, anchor="n")
        
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.text_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()
        
        # Added directions on how to delete items
        todo1 = tk.Label(self.tasks_frame, text="List Items --- **Right Click Item to Delete**", bg="midnightblue", fg="white", pady=10)
        todo1.bind("<Button-2>", self.remove_task) # Changed the delte task to the right mouse button
        
        self.tasks.append(todo1)
        
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)
            
        self.bind("<Return>", self.add_task)
        self.bind("<Configure>", self.on_frame_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>", self.task_width)
        
        self.colour_schemes = [{"bg": "midnightblue", "fg": "white"}, {"bg": "darkorange", "fg": "black"}] # Changed the color schemes for the items
    
    def create_menu(self):
        # Create menu bar
        menu_bar = tk.Menu(self)
        
        # Create File menu and add Exit option
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.exit_program)
        
        # Add File menu to menu bar
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Configure window to use the menu bar
        self.config(menu=menu_bar)
    
    def exit_program(self):
        # Confirm before quitting
        response = msg.askyesno("Exit", "Are you sure you want to exit?")
        if response:
            self.destroy() # Exit the program
        
    def add_task(self, event=None):
        task_text = self.task_create.get(1.0,tk.END).strip()
        
        if len(task_text) > 0:
            new_task = tk.Label(self.tasks_frame, text=task_text, pady=10)
            
            self.set_task_colour(len(self.tasks), new_task)
            
            new_task.bind("<Button-2>", self.remove_task)
            new_task.pack(side=tk.TOP, fill=tk.X)
            
            self.tasks.append(new_task)
            
        self.task_create.delete(1.0, tk.END)
    
    def remove_task(self, event):
        task = event.widget
        if msg.askyesno("Really Delete?", "Delete " + task.cget("text") + "?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()
            
    def recolour_tasks(self):
        for index, task in enumerate(self.tasks):
            self.set_task_colour(index, task)
            
    def set_task_colour(self, position, task):
        _, task_style_choice = divmod(position, 2)
        
        my_scheme_choice = self.colour_schemes[task_style_choice]
        
        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])
        
    def on_frame_configure(self, event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))
        
    def task_width(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.canvas_frame, width = canvas_width)
        
    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1
            
            self.tasks_canvas.yview_scroll(move, "units")
            
if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()