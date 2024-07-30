import json
import gspread
from google.oauth2.service_account import Credentials
from django.conf import settings


# Load credentials from settings
credentials_path = settings.GOOGLE_API_CREDENTIALS


with open(credentials_path) as f:
    credentials_info = json.load(f)


# Define the scope for the Google Sheets API
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Create a credentials object
credentials = Credentials.from_service_account_info(credentials_info, scopes=scope)


# Authenticate with Google Sheets API
gc = gspread.authorize(credentials)
# Open the spreadsheet by its ID; REPLACE WITH YOUR RESPECTIVE ID
spreadsheet_id = '11mICp6BjxUERrPsHbvA9oWdbgqTTfveZJM0MHAURRJI'
spreadsheet = gc.open_by_key(spreadsheet_id)


# Print the name of the spreadsheet
print(f'Spreadsheet name: {spreadsheet.title}')