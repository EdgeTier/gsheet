from .main import (
    gsheet_auth,
    gsheet_read,
    gsheet_write,
)

__all__ = [
    "gsheet_auth", 
    "gsheet_read", 
    "gsheet_write"
]

import sys, importlib
importlib.reload(sys.modules[__name__])


def printhi():
    print("alhamdolilah :)")