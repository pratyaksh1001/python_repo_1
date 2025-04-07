import pandas

def func1():
    try:
        name=list(input())
        data=pandas.read_csv("nato_phonetic_alphabet.csv")
        d={j.letter:j.code for (i,j) in data.iterrows()}
        for char in name:
            if char!=" ":
                print(char,d[char.upper()])
    except KeyError:
        print("the program can process alphabets only !")
        func1()
func1()