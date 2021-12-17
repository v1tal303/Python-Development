import config
import requests

#NUTRIX API

NUTR_ID = config.APP_ID
NUTR_KEY = config.API_KEY
NUTR_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

#SHEETY API

SHEETY_KEY = config.SHEETY_KEY
SHEETY_PROJECT = "workoutTracking"
SHEETY_SHEET = "workouts"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_KEY}/{SHEETY_PROJECT}/{SHEETY_SHEET}"


nutr_parameters = {
 "query":"ran 3 miles",
 "gender":"male",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

nutr_headers = {
 "x-app-id": NUTR_ID,
 "x-app-key": NUTR_KEY,

}

excercise_data = requests.post(url=NUTR_ENDPOINT, json=nutr_parameters, headers=nutr_headers)


print(SHEETY_ENDPOINT)
