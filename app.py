import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile
from main import *

root = tk.Tk()
canvas = tk.Canvas(root,width=600,height=300,bg = "red")
canvas.grid(columnspan = 3,rowspan = 3)

#inserting image
# logo = Image.open('404_image.jpg')
# logo = logo.resize((150, 250), Image.ANTIALIAS)
# logo = ImageTk.PhotoImage(logo)
# logo_label = tk.Label(image = logo)
# logo_label.image = logo
# logo_label.grid(column = 0,row = 0)


#instruction
instruction = tk.Label(root,text = "Select the python program to execute")
instruction.grid(column = 1,row = 1)



#global variable
file_path = ""

#file opening


def open_file():
    browse_text.set("Loading..")
    
    file = askopenfile(parent= root,mode = 'rb',title = "Choose a Python file",filetype = [('Python file',"*.py")])
    if file:
        browse_text.set("Browse")
        print("File opened successfully")
        #print(file.name) #pass this as a parameter to main.py

        global file_path
        file_path = file.name;

def locate_error():
    if(file_path == ""):
        messagebox.showerror("Error", "File not selected")
    program_name_list = file_path.split('/')
    program_name = program_name_list[-1]
    locate_stack_overflow(program_name)


#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root,textvariable = browse_text,command = lambda:open_file(),height=2,width=15,bg="green",fg = "white")
browse_text.set("Open File")
browse_btn.grid(column = 1,row = 2)

#Locate Error Button
error_text = tk.StringVar()
error_btn = tk.Button(root,textvariable = error_text,command = lambda:locate_error(),height=2,width=15,bg="green",fg = "white")
error_text.set("Locate Error")
error_btn.grid(column = 2,row = 2)


canvas = tk.Canvas(root,width=600,height=100,bg = "green")
canvas.grid(columnspan = 3)



root.mainloop()