from tkinter import * 
root = Tk()
from PIL import Image, ImageTk
import os
from tkinter import filedialog

root.title("Html_ide")
root.minsize(500,500)
root.maxsize(1000,1000)
root.config(background="light_pink")

exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))

label = Label(root, text="File name")
label.place(relx=0.28, rely=0.03, anchor=CENTER)

text_input = Entry(root)
text_input.place(relx=0.46, rely=0.3, anchor=CENTER)

text_area = Text(root, width=80, height=35)
text_area.place(relx=0.5, rely=0.5, anchor=CENTER)


name=""
def openFile() : 
    global name
    text_area.delete(1.0, END)
    text_input.delete(0, END)

    text_file= filedialog.askopenfilename(title="Files", filetypes=(("Text Files", "*.txt"),))
    name=os.path.basename(text_file)
    formatted_name= name.split(".")[0]
    text_input.insert(END, formatted_name)
    root.title(formatted_name)

    text_file= open(name, "r")
    p= text_file.read()
    text_area.insert(END, p)
    text_file.close()


open_btn = Button(root, image=open_img, command=openFile)
open_btn.place(relx=0.05, rely=0.03, anchor=CENTER)

save_btn = Button(root, image=save_img)
save_btn.place(relx=0.11, rely=0.03, anchor=CENTER)

exit_btn = Button(root, image=exit_img)
exit_btn.place(relx=0.17, rely=0.03, anchor=CENTER)



root.mainloop()