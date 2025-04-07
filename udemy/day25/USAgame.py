import pandas
import turtle
c=0
a=0
data=pandas.read_csv("50_states.csv")
states=[]
guessed=[]
for i in data["state"]:
    states.append(i.lower())
screen=turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
while c!=50:
    a+=1

    screen.title("USA game")
    image = ("blank_states_img.gif")
    screen.addshape(image)
    turtle.shape(image)
    answer = screen.textinput(f"Your score is: {c}/50", "Guess the state").title()
    if answer in data["state"].to_list() and answer not in guessed:
        guessed.append(answer)
        t.penup()
        t.goto(int(data[data["state"] == answer]["x"]), int(data[data["state"] == answer]["y"]))
        t.pendown()
        t.write(arg=answer)
        c+=1
    if answer=="End":
        break
not_guesed=[i for i in states if i not in guessed]
d={"not_guessed":not_guesed}
generated=pandas.DataFrame(d)
data2=pandas.read_csv("Usa_game_result.csv")
print(data2["Not guessed"])
generated.to_csv("Usa_game_result.csv")
turtle.mainloop()