import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()


# Creating apps list
apps = []

# Storing the paths which are saved in text file to an array
if os.path.isfile('saved_apps.txt'):
    with open('saved_apps.txt','r') as f:
        temp_apps = f.read()
        temp_apps = temp_apps.split(",")

        # This will remove the blank spaces which occurred because we did not 
        # enter any app after clicking open
        apps= [x for x in temp_apps if x.strip() ]


# Creating button for adding apps
def add_apps():

    # removing duplaicate app direcotries
    for widget in frame.winfo_children():
        widget.destroy()

    file_name =  filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables","*.exe"),("all files","*,*")))

    # Adding multiple apps in the list
    apps.append(file_name)
    print(file_name)

    # iterate over the list of apps
    for app in apps:
        label =tk.Label(frame, text = app ,bg="#f9f9f9")
        label.pack()


# Running apps
def run_apps():
    for app in apps:
        os.startfile(app)


# resizing canvas
canvas = tk.Canvas(root,height=500,width =450, bg="#007FC6")
#007FC6

# attaching the canvas to root
canvas.pack()

# creating frame
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8,relx=0.1,rely= 0.1 )

# creating buttons
open_file = tk.Button(root,text="Open file", padx=10,pady=5,fg="white",bg="#007FC6", command = add_apps)

# attaching buttons to frame
open_file.pack()

run_apps = tk.Button(root,text="Run apps", padx=10,pady=5,fg="white",bg="#007FC6",command = run_apps )
run_apps.pack()


# for printing the apps present in saved.txt, on frame 
for app in apps:
    label= tk.Label(frame, text = app)
    label.pack()


# opening window
root.mainloop()



# Saving our lists of apps for opening the app after execution
with open('saved_apps.txt','w') as f:
    for app in apps:
        f.write(app + ",")