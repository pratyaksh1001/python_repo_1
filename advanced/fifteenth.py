MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            #"milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
while 1:
    for i in MENU.keys():
        print(f"the cost of {i} = {MENU[i]['cost']}")
    x=input("enter which coffee you want: ")
    f = ""
    for i in resources.keys():
        try:
            if resources[i] >= MENU[x]["ingredients"][i]:
                continue
            else:
                f = MENU[x]["ingredients"][i]
                print(f"sorry we lack in {f}")
                break
        except:
            continue
    penny=0.01*(int(input("enter pennies: ")))
    dime=0.1*(int(input("enter dimes: ")))
    nickel=0.05*(int(input("enter nickels: ")))
    quarter=0.25*(int(input("enter quarters: ")))
    total=penny+dime+quarter+nickel
    if MENU[x]["cost"]>total:
        print("the money is not sufficient !")
    elif MENU[x]["cost"]<total:
        print("your coffee is ready !")
        print(f"here's the change: {total-MENU[x]['cost']}")
        for i in resources.keys():
            try:
                resources[i] -= MENU[x]["ingredients"][i]
            except:
                continue
    else:
        print("your coffee is ready !")
        for i in resources.keys():
            try:
                resources[i] -= MENU[x]["ingredients"][i]
            except:
                continue
    print("the resources available are: ")
    for i in resources:
        print(f"{i} - {resources[i]}")
    print()