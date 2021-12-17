import config
import requests
from datetime import datetime

# NUTRIX API

NUTR_ID = config.APP_ID
NUTR_KEY = config.API_KEY
NUTR_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# SHEETY API

SHEETY_KEY = config.SHEETY_KEY
SHEETY_PROJECT = "workoutTracking"
SHEETY_SHEET = "workouts"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_KEY}/{SHEETY_PROJECT}/{SHEETY_SHEET}"
SHEETY_AUTH = config.SHEETY_AUTH

user_input = input("What excercise did you do today? ")

# Query the Nutritionix

nutr_parameters = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 174,
    "age": 27
}

nutr_headers = {
    "x-app-id": NUTR_ID,
    "x-app-key": NUTR_KEY,
    "Content-Type": "application/json"
}

exercise_data = requests.post(url=NUTR_ENDPOINT, json=nutr_parameters, headers=nutr_headers)

# Nutritionix response json data

exercise_type = exercise_data.json()["exercises"][0]["name"].capitalize()
exercise_duration = exercise_data.json()["exercises"][0]["duration_min"]
exercise_calories = exercise_data.json()["exercises"][0]["nf_calories"]

# Get today's date and time

today = datetime.now()
today_str = today.strftime("%d/%m/%Y")
today_hours = today.strftime("%H:%M:%S")

# Sheety Parameters

workout_header = {
    "Content-Type": "application/json",
    "Authorization": SHEETY_AUTH,
}

new_workout = {
    "workout": {
        "date": today_str,
        "time": today_hours,
        "exercise": exercise_type,
        "duration": exercise_duration,
        "calories": exercise_calories,
    }
}

# Sheety post

sheety_new_row = requests.post(url=SHEETY_ENDPOINT, json=new_workout, headers=workout_header)

print(sheety_new_row.text)
