from setuptools import setup


setup(
    name="gsheet",
    version="3.1.3",
    description="Import and Export DataFrames to Google Sheets",
    packages=["gsheet"],
    install_requires=[
        "pandas", 
        "gspread"
    ],
)