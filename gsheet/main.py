import pandas as pd
from gspread import (
    service_account,
    Client,
    WorksheetNotFound,
) 


gaccount: Client|None = None


def gsheet_auth(credentials_path = "credentials.json"):
    global gaccount
    gaccount = service_account(credentials_path)


def gsheet_read(sheet_url, worksheet_name = None):
    if gaccount is None:
        raise RuntimeError("Authenticate Account first using gsheet_auth()")
    
    file = gaccount.open_by_url(sheet_url)
    worksheet = file.worksheet(worksheet_name)
        
    return pd.DataFrame(worksheet.get_all_records())


def gsheet_write(df, sheet_url, worksheet_name = None):
    if gaccount is None:
        raise RuntimeError("Authenticate Account first using gsheet_auth()")
    
    file = gaccount.open_by_url(sheet_url)
    
    try:
        worksheet = file.worksheet(worksheet_name)
        worksheet.clear()
        
    except WorksheetNotFound:
        worksheet = file.add_worksheet(title=worksheet_name, rows=None, cols=None)
        
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

