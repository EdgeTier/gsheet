from setuptools import setup


setup(
    name="gsheet",
    version="1.0.0",
    description="Import and Export DataFrames to Google Sheets",
    packages=["gsheet"],
    install_requires=[
        "pandas", 
        "gspread"
    ],
)