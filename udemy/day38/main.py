import requests
import json
APP_ID = "cfa2206b"
APP_KEY = "83aca783b249312986263da9e1c246b0"
END_POINT_NUTRITION = "https://trackapi.nutritionix.com/v2/natural/nutrients"
END_POINT_EXERCISE = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
exercise = input("enter the exercise: ")
exercise_data = {
    "query": exercise
}
food = input("enter the food: ")
file = open("exercise.json", "w")
file2 = open("food.json", "w")
food_data = {
    "query": food
}
connection1 = requests.post(url=END_POINT_EXERCISE, headers=header, json=exercise_data)
connection2 = requests.post(url=END_POINT_NUTRITION, headers=header, json=food_data)
print(f"you can eat {connection1.json()["exercises"][0]["nf_calories"] // connection2.json()["foods"][0]["nf_calories"]} {food}")
json.dump(connection1.json(), file, indent=4)
json.dump(connection2.json(), file2, indent=4)
