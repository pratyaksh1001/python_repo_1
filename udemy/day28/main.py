from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
window=Tk()
timecount=10
class time:
    def __init__(self,m,s):
        self.min=m+(s//60)
        self.sec=s%60
    def decrease(self,x):

        if self.sec==0:
            self.sec=59
            self.min-=1
        else:
            self.sec -= 1
        canvas.itemconfig(time_text, text=f"{TIME.min}:{TIME.sec}")

TIME=time(WORK_MIN,0)
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window.title("Pomodoro")
lt=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
lt.grid(row=0,column=1)
window.config(bg=YELLOW)
canvas=Canvas(width=200,height=224)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tomato)
canvas.config(bg=YELLOW)
canvas.grid(row=1,column=1)
time_text=canvas.create_text(103,130,text=timecount,fill="white",font=(FONT_NAME,35,"bold"))
window.config(padx=100,pady=50)
reset=Button(text="Reset",bg=PINK)
reset.grid(row=3,column=2)
start=Button(text="Start",bg=PINK)
start.grid(row=3,column=0)
ticks="✔"
tick=Label(text=ticks,bg=YELLOW,fg=RED)
tick.grid(row=3,column=1)
window.after(1000,TIME.decrease(1))
window.mainloop()