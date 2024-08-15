import pandas as pd
import gspread
from gspread.exceptions import WorksheetNotFound


gc = None


def gsheet_auth(credentials_path = "credentials.json"):
    global gc
    gc = gspread.service_account(credentials_path)


def read_gsheet(sheet_url, worksheet_name = None):
    file = gc.open_by_url(sheet_url)
    worksheet = file.worksheet(worksheet_name)
        
    return pd.DataFrame(worksheet.get_all_records())


def write_gsheet(df, sheet_url, worksheet_name = None):
    file = gc.open_by_url(sheet_url)
    
    try:
        worksheet = file.worksheet(worksheet_name)
        worksheet.clear()
        
    except WorksheetNotFound:
        worksheet = file.add_worksheet(title=worksheet_name, rows=None, cols=None)
        
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
