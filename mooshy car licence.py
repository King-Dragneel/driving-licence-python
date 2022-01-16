from tkinter import *

root = Tk()

root.title("Driving Licence")
root.geometry("300x400")

root.configure(bg="White")
canvas=Canvas(root,width=300,height=400)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150,90, font=('Times', '24', 'bold italic') ,text="Driving Licence")
label_name_tag = canvas.create_text(40,165, font=('Times', '16', 'bold') ,text="Name :")
label_job_tag = canvas.create_text(40,205, font=('Times', '16', 'bold') ,text="Job :")
label_subjects_tag = canvas.create_text(50,250, font=('Times', '16', 'bold') ,text="Subjects :")

label_name = Label(root)
label_job = Label(root)
label_subjects = Label(root)

def myCardDetails():
    name = "Max MoOshy Gosain"
    print(type(name))   
    job = "Professor "
    print(type(job))
    subjects = "Bunnyleg Science,Nose Biology"
    print(type(subjects))
    
    label_name['text'] = name
    label_job['text'] = job
    label_subjects['text'] = subjects
    
    
button1 = Button(root, text = "Show my ID Card", command=myCardDetails)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=label_name)
label_job_window = canvas.create_window(90, 205, anchor=CENTER, window=label_job)
label_subjects_window = canvas.create_window(155, 252, anchor=CENTER, window=label_subjects)
canvas.pack()

root.mainloop()