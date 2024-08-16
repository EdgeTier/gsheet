from setuptools import setup
from pathlib import Path

# The directory containing this file
HERE = Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gsheet",
    version="1.0.0",
    description="Import and Export DataFrames to Google Sheets",
    # long_description=README,
    # long_description_content_type="text/markdown",
    # url="https://github.com/EdgeTier/gsheet",
    # author="EdgeTier",
    packages=["gsheet"],
    # include_package_data=True,
    install_requires=[
        "pandas", 
        "gspread"
    ],
)