import requests
end_point=f"https://pixe.la/v1/users"
token="Pratyaksh_102080"
username="pratyaksh"

graph_config={
    "id":"graph2",
    "name":"graph2",
    "unit":"coding",
    "type":"float",
    "color":"momiji"
}
header={
    "X-USER-TOKEN":token
}
connection=requests.post(url=f"{end_point}/{username}/graphs",json=graph_config,headers=header)
print(connection)