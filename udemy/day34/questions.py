import requests
import random
import html
response=requests.get(url="https://opentdb.com/api.php?amount=10&category=17&difficulty=easy")
S=0
E=0
def run(i):
    data=response.json()["results"][i]
    question=data["question"]
    options=[]
    options.extend(data["incorrect_answers"])
    options.append(data["correct_answer"])
    random.shuffle(options)
    answer=data["correct_answer"]
    return {"question":html.unescape(question),"options":options,"answer":answer}
abcd="ABCD"
while E!=10:
    x=run(E)
    print(x["question"])
    ind=x["options"].index(x["answer"])
    for i in range(len(x["options"])):
        print(f"{abcd[i]} : {x["options"][i]}")
    inp=input("enter the correct option: ").upper()
    if inp==abcd[ind]:
        print("correct !")
        S+=1
    else:
        print("Incorrect !")
        print(f"the correct answer is: {abcd[ind]} : {x["options"][ind]}")
    E+=1
    print(f"Your Score is: {S}/{E}")
    print("\n_______________________________________________________\n")