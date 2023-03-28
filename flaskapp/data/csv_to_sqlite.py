from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, types


# Define the database file name and location
db_file = Path(__file__).parent.joinpath("database.db")

# Create a connection to file as a SQLite database (this automatically creates the file if it doesn't exist)
engine = create_engine("sqlite:///" + str(db_file), echo=False)


first = Path(__file__).parent.joinpath("after prepare.xlsx")
expenditure = pd.read_excel(first,sheet_name = "expenditure")

second = Path(__file__).parent.joinpath("after prepare.xlsx")
enrolment = pd.read_excel(second,sheet_name = "enrolment")

third = Path(__file__).parent.joinpath("after prepare.xlsx")
institutional_distribution = pd.read_excel(third,sheet_name = "institutional_distribution")

# Write the data to tables in a sqlite database
dtype_expenditure = {
    "Years": types.INTEGER(),
    "Current_prices": types.FLOAT(),
    "Education_Price_Index": types.FLOAT(),
    "Constant_1990_prices": types.FLOAT(),
}

dtype_enrolment = {
    "Years": types.INTEGER(),
    "TOTAL": types.FLOAT(),
    "Primaire": types.FLOAT(),
    "Secondaire": types.FLOAT(),
    "Higher_education": types.FLOAT(),
    "Special": types.FLOAT(),
    "Further_Education": types.FLOAT(),
}

dtype_id = {
    "Years": types.INTEGER(),
    "TOTAL": types.FLOAT(),
    "Central_Government": types.FLOAT(),
    "LEA": types.FLOAT(),
    "UGC": types.FLOAT(), 
}

expenditure.to_sql(
    "expenditure", engine, if_exists="append", index=False, dtype=dtype_expenditure
)
enrolment.to_sql(
    "enrolment", engine, if_exists="append", index=False, dtype=dtype_enrolment
)
institutional_distribution.to_sql(
    "institutional_distribution", engine, if_exists="append", index=False, dtype=dtype_id
)