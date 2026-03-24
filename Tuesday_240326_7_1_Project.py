import pandas as pd
import sqlite3 as sql
import os 

df = pd.read_csv("StudentPerformanceFactors.csv")

def clean(df):
    df=df.drop_duplicates().copy()
    df.loc[:,"Parental_Involvement"]=(
        df["Parental_Involvement"]
        .str.upper()
        .replace({"LOW": "L","MEDIUM": "M","HIGH": "H"})
    )
    df.loc[:,"Access_to_Resources"]=(
        df["Access_to_Resources"]
        .str.upper()
        .replace({"LOW": "L","MEDIUM": "M","HIGH": "H"})
    )
    return df

def load(conn):
    if os.path.exists("student.db"):
        os.remove("student.db")
    conn = sql.connect("student.db")
    df.to_sql("Students",conn,if_exists="replace",index=False)
    return conn

df_cleaned = clean(df)
conn = load(df_cleaned)

query = '''Select * from Students'''
result = pd.read_sql(query,conn)
print(result)

conn.close()