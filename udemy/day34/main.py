import tkinter as tk
import questions
SCORE=0
Q=0
screen=tk.Tk()
screen.title("Quiz Application Using Trivia API and Tkinter")
screen.minsize(width=800,height=400)
canvas1=tk.Canvas(screen,width=390,height=390,bg="blue")
canvas2=tk.Canvas(screen,width=390,height=390,bg="green")
l1=tk.Label(screen,text=f"The question is:\n{questions.run(Q)['question']}",font=("consolas",12,"bold"),bg="green",width=50,height=20)
l1.grid(row=0,column=0)
l2=tk.Label(screen,text=f"Select the correct option: ")
l2.grid(row=0,column=1)
screen.mainloop()

# TODO day 34 is not completed
