import sqlite3 as sql
import pandas as pd
import os

try:
    df = pd.read_csv("Employee.csv")
except:
    print("No file found")

def clean(df):
    df = df.drop_duplicates().copy()
    df.columns = (df.columns.str.replace(r'(?<!^)(?=[A-Z])', '_', regex=True))
    df.loc[:,"Education"] = (df["Education"]
                             .str.strip()
                             .replace({"Bachelors" : "BA","Masters" : "MA"} )
                             )
    df.loc[:,"Gender"] = (df["Gender"]
                             .str.strip()
                             .replace({"Male" : "M","Female" : "F"} )
                             )
    df.loc[:,"Age"] = (
        pd.to_numeric(df["Age"],errors="coerce")
    )
    df.loc[:,"City"] = df["City"].fillna("Unknown")
    return df

def load(df):
    if os.path.exists("employees.db"):
        os.remove("employees.db")
        conn = sql.connect("employees.db")
        df.to_sql("Employees",conn,if_exists="replace",index=False)
        return conn

def pipeline(df, query= "Select * from Employees"):
    cleaned_df = clean(df)
    conn = load(cleaned_df)
    result = pd.read_sql(query, conn)
    return result

result = pipeline(df)
print(result)

