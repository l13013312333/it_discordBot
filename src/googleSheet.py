import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def sheet_init(sheetID):
    filePath = ".data/credentials.json"
    scopes = ["https://spreadsheets.google.com/feeds"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
     filePath, scopes)
    client = gspread.authorize(credentials)
    excel = client.open_by_key(os.getenv("GOOGLE_SHEET_ID"))
    return excel.worksheet(sheetID)


def get_sheet(sheetID):
    sheet = sheet_init(sheetID)
    return sheet.get_all_records()


def add_row_sheet(sheetID, data):
    sheet = sheet_init(sheetID)
    return sheet.append_row(data, table_range="A1")
