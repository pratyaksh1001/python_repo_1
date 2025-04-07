import requests
import datetime as dt
end_point = f"https://pixe.la/v1/users"
token = "Pratyaksh_102080"
username = "pratyaksh"
header = {
    "X-USER-TOKEN": token
}
graph_id = "graph2"
pixel_url = f"{end_point}/{username}/graphs/{graph_id}"
today = dt.date.today()# - dt.timedelta(days=1)
if today.month < 10:
    x = f"0{today.month}"
else:
    x = f"{today.month}"
pixel_config = {
    "date": f"{today.year}{x}{today.day}",
    "quantity": input()
}
print(pixel_config)
pixel_req = requests.post(url=pixel_url, json=pixel_config, headers=header)
print(pixel_req)