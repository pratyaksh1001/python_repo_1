import requests
import time
def generate():
    response = requests.get(url="https://api.kanye.rest/")
    print(response.json()["quote"])
    print()
x=input("enter yes to get quote: ")
while x=="yes":
    generate()
    time.sleep(5)