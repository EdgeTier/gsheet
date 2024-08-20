# 📊 GSheet

Import and Export Pandas DataFrames to Google Sheets effortlessly


## 🚀 How to Use
```bash
$ pip install -I https://github.com/EdgeTier/gsheet/archive/master.zip
```

```python
import gsheet

gsheet.auth("/path/to/credentials/")

df = gsheet.read("https://docs.google.com/spreadsheets/.....")

gsheet.write(df, "https://docs.google.com/spreadsheets/.....", "new_sheet")
```

**Note:** When using Jupyter Notebook, GSheet must be manually reloaded to reflect new changes to package. See [below](#jupyter-notebook)


## 📝 Documentation
#### `gsheet.auth()`
* Requires path to `credentials.json` which contain Google Sheets API keys
* `credentials.json` may be found in root of SageMaker Notebook
* File must be shared with `client_email` found in `credentials.json`

#### `gsheet.read()`
* Reads single Worksheet from Google Sheets file and converts it to a DataFrame
* Assumes Row 1 is Header row
* Data must start from A1
* Defaults to reading first Worksheet if no Worksheet name provided

#### `gsheet.write()`
* Writes DataFrame to Google Sheet.
* Creates/Replaces worksheet if name provided
* Creates new worksheet with default name (eg. Sheet5) if no name provided


## 🔄 How to Update Package

1. Ensure any new dependencies are added to `setup.py`
    ```python
    setup(
        ...
        install_requires=[
            "pandas", 
            "gspread"
        ],
        ...
    )
    ```

2. Push new changes to _Master_ Branch on [Github](https://github.com/EdgeTier/gsheet)

#### Jupyter Notebook
When using Jupyter Notebook, new changes won't be reflected automatically after updating package. Either restart kernel each time or reload the package.

```python
import gsheet

# How to reload package
import importlib
importlib.reload(gsheet)
```