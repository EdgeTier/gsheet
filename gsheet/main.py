import pandas as pd
from gspread import (
    service_account,
    Client,
    WorksheetNotFound,
) 


gaccount: Client | None = None


def auth(credentials_path: str = "credentials.json") -> None:
    """
    Authenticate Google Account using credentials JSON file. 
    Must also share Google Sheet with client_email (found in JSON).

    :param credentials_path: Path to credentials JSON file.
    """
    global gaccount
    gaccount = service_account(credentials_path)


def read(sheet_url: str, worksheet_name: str | None = None) -> pd.DataFrame:
    """
    Reads single Worksheet from Google Sheets file as DataFrame.
    Assumes data starts from A1 and row 1 is header row.

    :param sheet_url: Full URL to Google Sheet. File must be shared with client_email.
    :param worksheet_name: Worksheet name. (Default is first Worksheet in File)
    :returns: Worksheet as DataFrame.
    :raises RuntimeError: if Google Account isn't authenticated.
    """
    if gaccount is None:
        raise RuntimeError("Authenticate Account first using gsheet.auth()")
    
    file = gaccount.open_by_url(sheet_url)

    if worksheet_name is None:
        # Open first worksheet, usually Sheet1
        worksheet = file.get_worksheet(0)
    else:
        worksheet = file.worksheet(worksheet_name)
        
    return pd.DataFrame(worksheet.get_all_records())


def write(df: pd.DataFrame, sheet_url: str, worksheet_name: str | None = None) -> None:
    """
    Writes DataFrame to Google Sheets by creating/replacing Worksheet.

    :param df: DataFrame.
    :param sheet_url: Full URL to Google Sheet. File must be shared with client_email.
    :param worksheet_name: Worksheet to replace or creates new one if left blank.
    :raises RuntimeError: if Google Account isn't authenticated.
    """
    if gaccount is None:
        raise RuntimeError("Authenticate Account first using gsheet.auth()")
    
    file = gaccount.open_by_url(sheet_url)
    
    try:
        worksheet = file.worksheet(worksheet_name)
        worksheet.clear()
        
    except WorksheetNotFound:
        # Rows/Cols are None to create worksheet with default size (26 x 1000)
        worksheet = file.add_worksheet(title=worksheet_name, rows=None, cols=None)
        
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())