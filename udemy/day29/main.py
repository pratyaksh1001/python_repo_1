from tkinter import *
from tkinter import messagebox
import random as r
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    s=""
    chars=["abcdefghijklmnopqrstuvwxyz","1234567890","!@#$%&*?","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for i in range(16):
        x=r.randrange(0,4)
        s+=r.choice(chars[x])
    inp3.config()
    inp3.insert(0,s)
# ---------------------------- SAVE PASSWORD ------------------------------- #


file=open("passwords.txt","a")

def addpass():
    if len(inp1.get())==0 or len(inp2.get())==0 or len(inp3.get())==0:
        messagebox.showerror(message="Fill all the fields properly",title="Password Manager")
    else:
        l = f"{inp1.get()} | {inp3.get()} | {inp2.get()}\n"
        x = messagebox.askokcancel(title="Confirmation", message=f"{l} is correct input or not ?")
        if x:
            file.write(l)
        else:
            messagebox.showinfo(message="Re-enter the details")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.config(padx=20,pady=20)
window.title("Password Manager")
window.minsize(200,200)
canvas=Canvas(height=200,width=200)
image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)
btn1=Button(text="Generate",command=generate,width=10)
btn1.grid(row=3,column=2)
btn2=Button(text="Add",command=addpass,width=50)
btn2.grid(row=4,column=0,columnspan=3)
l1=Label(text="email")
l1.grid(row=1,column=0)
inp1=Entry(width=40)
inp1.grid(row=1,column=1,columnspan=2)
l2=Label(text="Website")
l2.grid(row=2,column=0)
inp2=Entry(width=40)
inp2.grid(row=2,column=1,columnspan=2)
WEBSITE=inp2.get()
l3=Label(text="password")
l3.grid(row=3,column=0)
inp3=Entry(width=25)
inp3.grid(row=3,column=1)
window.mainloop()