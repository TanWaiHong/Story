import requests
from datetime import datetime


USERNAME = "hongttisme"
TOKEN = "biui4niubi3nig1b23bj32b"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Update a user

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "X-USER-TOKEN": TOKEN,
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",

}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

# response = requests.post(url=pixel_post_endpoint, headers=headers, json=pixel_post_config)
# print(response.text)

pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_put_config = {
    "quantity": "2",
}

# response = requests.put(url=pixel_put_endpoint, headers=headers, json=pixel_put_config)
# print(response.text)

pixel_delete_endpoint = pixel_put_endpoint

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)
