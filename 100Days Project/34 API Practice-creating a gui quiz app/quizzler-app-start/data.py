import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

question_response = requests.get("https://opentdb.com/api.php", params=parameters)
question_response.raise_for_status()
question_data = question_response.json()['results']

