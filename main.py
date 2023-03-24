import requests
from datetime import date

USERNAME = "bethj"
TOKEN = "azertyqq"
GRAPH_ID= "languagegraph1"
pixela_endpoint = "https://pixe.la/v1/users"
today = date.today().strftime('%Y%m%d')

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# Create user (only once)
# response= requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "language study",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu"
}
# Create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": "20230323",
    "quantity": "20"
}
# Add today's pixel to the graph
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)

# Udate and delete a pixel on the graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230323"
update_config = {
    "quantity": "15.0"
}
#response = requests.post(url=update_endpoint, json=update_config)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230323"
# response = requests.post(url=delete_endpoint, headers=headers)
print(response.text)