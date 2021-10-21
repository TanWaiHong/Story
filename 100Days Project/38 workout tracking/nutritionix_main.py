import os
import requests
import datetime as dt

GENDER = "male"
WEIGHT_KG = 76
HEIGHT_CM = 172
AGE = 17

APP_ID = os.getenv("NUTRITIONIX_ID")
API_KEY = os.getenv("NUTRITIONIX_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.getenv("YOUR_SHEET_ENDPOINT")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
data = response.json()

today = dt.datetime.today()
TOKEN = "Bearer 0j02hh8fj20jvg0h"
project = "1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494"

for exercise in data["exercises"]:

    sheet_post_headers = {
        "Authorization": TOKEN,
    }

    body = {
        'sheet1': {
            'date': today.strftime("%d/%m/%Y"),
            'time': today.strftime("%X"),
            'exercise': exercise['user_input'],
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
            'id': exercise['tag_id']
        }
    }

    response = requests.post(
        url=SHEET_ENDPOINT,
        headers=sheet_post_headers,
        json=body
    )

    print(response.json())
