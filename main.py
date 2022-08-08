#Pixela Habit Tracker

import requests
from datetime import datetime

USER =  "yami001"
TOKEN_ADD = "!@#$%QWERTYUIOP"

#create user
USER_ENDPOINT = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN_ADD,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

#Only runs once to create username

# response =requests.post(url = USER_ENDPOINT, json=user_parameters)
# print(response.text)


#Create graph
GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USER}/graphs"
graph_params = {
    "id": "graph1",
    "name": "graph1",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN_ADD
}
#Can only create one graph with one grath ID
# r = requests.post(url=GRAPH_ENDPOINT, json= graph_params, headers= header)


#POst a pixel in the graph
PIXEL_ENDPOINT = f"{USER_ENDPOINT}/{USER}/graphs/graph1"
today = datetime.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}
pixel_resp = requests.post(url = PIXEL_ENDPOINT, json= pixel_params, headers= header)
print(pixel_resp.text)



#Update a Pixel in the graph
update_params = {
    "quantity": "7"
}
UPDATE_ENDPOINT = f"{PIXEL_ENDPOINT}/{today.strftime('%Y%m%d')}"
# update_resp = requests.put(url= UPDATE_ENDPOINT, json= update_params, headers= header )
# print(update_resp.text)



#Delete a pixel from the graph
DELETE_ENDPOINT = UPDATE_ENDPOINT
# delete_resp = requests.delete(url = DELETE_ENDPOINT, headers= header)
# print(delete_resp)