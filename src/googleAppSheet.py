import os
import requests


# google appsheet
def app_sheet_init(tableId, payload):
  appId = os.getenv("GOOGLE_APPSHEET_ID")
  url = f'https://api.appsheet.com/api/v2/apps/{appId}/tables/{tableId}/Action'
  headers = {'ApplicationAccessKey': os.getenv("GOOGLE_APPSHEET_TOKEN")}
  
  x = requests.post(url, headers=headers, json=payload)
  return x.text

def app_sheet_find(tableId, selector):
  return app_sheet_init(tableId, {
    "Action": "Find",
    "Properties": { 
      "Locale": "zh-tw",
      "Selector": selector
    },
  })

def app_sheet_add(tableId, data):
  payload = {
    "Action": "Add",
    "Properties": { "Locale": "zh-tw" },
    "Rows": [ data ]
  }
  app_sheet_init(tableId, payload)

def app_sheet_edit(tableId, data):
  payload = {
    "Action": "Edit",
    "Properties": { "Locale": "zh-tw" },
    "Rows": [ data ]
  }
  app_sheet_init(tableId, payload)