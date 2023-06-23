import gspread
from oauth2client.service_account import ServiceAccountCredentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "./configs/gsheets.json", scopes=scopes)
file = gspread.authorize(creds)
workbook = file.open("ANPR")
sheet = workbook.sheet1


def append_data(plate, date, time, state):
    sheet.append_row([plate, date, time, state])


def fetch_data():
    return sheet.get_all_records()


def execute_query(query_plate):
    query_plate_cpy = query_plate.replace(" ", "")
    message = ""
    result = {}
    flag = 0
    for record in sheet.get_all_records():
        if record['Registration_Number'].replace(" ", "") == query_plate_cpy:
            flag = 1
            message = "Success"
            result = record
            break
    if flag == 0:
        message = "Fail"
    return message, result
