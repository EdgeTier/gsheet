import pandas as pd
from gspread import (
    service_account,
    Client,
    WorksheetNotFound,
) 


gaccount: Client | None = None


def auth(credentials_path: str = "credentials.json") -> None:
    global gaccount
    gaccount = service_account(credentials_path)


def read(sheet_url: str, worksheet_name: str | None = None) -> pd.DataFrame:
    if gaccount is None:
        raise RuntimeError("Authenticate Account first using auth()")
    
    file = gaccount.open_by_url(sheet_url)

    if worksheet_name is None:
        worksheet = file.get_worksheet(0)
    else:
        worksheet = file.worksheet(worksheet_name)
        
    return pd.DataFrame(worksheet.get_all_records())


def write(df: pd.DataFrame, sheet_url: str, worksheet_name: str | None = None) -> None:
    if gaccount is None:
        raise RuntimeError("Authenticate Account first using auth()")
    
    file = gaccount.open_by_url(sheet_url)
    
    try:
        worksheet = file.worksheet(worksheet_name)
        worksheet.clear()
        
    except WorksheetNotFound:
        worksheet = file.add_worksheet(title=worksheet_name, rows=None, cols=None)
        
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())