import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

OPENAI_API_KEY = ''
with open("./configs/openAI.json") as file:
    data = json.load(file)
    OPENAI_API_KEY = data["OPENAI_API_KEY"]

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "./configs/gsheets.json", scopes=scopes)
file = gspread.authorize(creds)
workbook = file.open("ANPR")
sheet = workbook.sheet1
records = sheet.get_all_records()

model = 'text-davinci-003'
openai.api_key = OPENAI_API_KEY


def ask(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="{0} in {1}".format(message, records),
        temperature=0.7,
        max_tokens=120,
        top_p=0.9,
        frequency_penalty=0.0,
        presence_penalty=1
    )
    return str(response["choices"][0]["text"])
