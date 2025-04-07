import requests
end_point = f"https://pixe.la/v1/users"
token = "Pratyaksh_102080"
username = "pratyaksh"
header = {
    "X-USER-TOKEN": token
}
graph_id = "graph2"
date = input("enter the date in yyyymmdd: ")
pixel_url = f"{end_point}/{username}/graphs/{graph_id}"
update_url = f"{end_point}/{username}/graphs/{graph_id}/{date}"
updated_data = {
    "quantity": input("enter the data you want to update: ")
}
connection=requests.put(url=update_url, headers=header, json=updated_data)
print(connection)