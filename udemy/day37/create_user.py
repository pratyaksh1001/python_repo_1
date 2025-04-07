import requests
end_point=f"https://pixe.la/v1/users"
x=input("enter the number: ")
print(x)
parameters={
    "token":"Pratyaksh_102080",
    "username":"pratyaksh",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
connection=requests.post(url=end_point,json=parameters)
print(connection.json())
# the user is created
