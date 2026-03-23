import pandas as pd
import sqlite3 as sql
import os

# First, read the CSV file
df = pd.read_csv("Employee.csv")

def clean(df):
    df = df.drop_duplicates().copy()
    df.loc[:, "Education"] = (
        df["Education"]
        .str.strip()
        .str.upper()
        .replace({"BACHELORS": "BA", "MASTERS": "MA"})
    )
    df.loc[:, "Gender"] = (
        df["Gender"]
        .str.strip()
        .str.upper()
        .replace({"MALE": "M", "FEMALE": "F"})
    )
    df.columns = df.columns.str.replace(" ", "_").str.capitalize()
    print("Data Cleansed")
    return df

def load(df):
    if os.path.exists("employees.db"):
        os.remove("employees.db")
    conn = sql.connect("employees.db")
    df.to_sql("Employees", conn, if_exists="replace", index=False)
    print("Data Loaded")
    return conn

# Clean the data and load to database
df_cleaned = clean(df)
conn = load(df_cleaned)

# Query and display results
query = """SELECT * FROM Employees"""
result = pd.read_sql(query, conn)
print(result)

# Close the connection
conn.close()