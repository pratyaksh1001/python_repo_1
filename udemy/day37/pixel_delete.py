import requests
end_point = f"https://pixe.la/v1/users"
token = "Pratyaksh_102080"
username = "pratyaksh"
header = {
    "X-USER-TOKEN": token
}
graph_id = "graph2"
date = input("enter the date in yyyymmdd: ")
delete_url=f"{end_point}/{username}/graphs/{graph_id}/{date}"
connection=requests.delete(url=delete_url,headers=header)
print(connection)