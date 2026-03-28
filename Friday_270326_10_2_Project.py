import pandas as pd
import os
import sqlite3 as sql

df = pd.read_csv("Employee.csv")

def clean(df):
    df=df.drop_duplicates().copy()
    df.columns = (df.columns.str.replace(r'(?<!^)(?=[A-Z])', '_', regex=True))
    df.loc[:,"City"] = df["City"].fillna("Unknown")
    df.loc[:,"Education"] = (
        df["Education"]
        .str.strip()
        .replace({"Bachelors":"BA","Masters":"MA"})
    )
    df.loc[:,"Gender"] = (
        df["Gender"]
        .str.strip()
        .replace({"Male": "M", "Female": "F"})
    )
    df.loc[:,"Age"] = pd.to_numeric(df["Age"],errors="coerce")
    df.loc[:,"Experience_In_Current_Domain"] = (
        pd.to_numeric(df["Experience_In_Current_Domain"],errors="coerce")
    )
    df.loc[:,"Leave_Or_Not"] = (

        pd.to_numeric(df["Leave_Or_Not"],errors="coerce")
    )
    df.loc[:,"Payment_Tier"] = (
        pd.to_numeric(df["Payment_Tier"],errors="coerce")
    )
    df.loc[:,"Joining_Year"] = (
        pd.to_numeric(df["Joining_Year"],errors="coerce")
    )
    return df
   
def load(df):
    if os.path.exists("employees.db"):
        os.remove("employees.db")
    conn = sql.connect("employees.db")
    df.to_sql("Employees",conn,if_exists="replace",index=False)
    return conn

def validate(conn,query= "Select * from Employees"):
    result = pd.read_sql(query, conn)
    return result


def pipline_runner(df,steps):
    clean_df = None
    conn = None
    result = None
    for step in steps:
      if step == clean:
        clean_df = step(df)
      elif step == load:
        if clean_df != None:
         conn = step(clean_df)
        else:
         conn = step(df)
      elif step == validate:
        if conn != None:
            result = step(conn)
        else:
         print("No data to validate")
         return None
        
    if result is not None: return result
    elif conn is not None: return conn
    elif clean_df is not None: return clean_df
    else: return df

steps = [clean]
result = pipline_runner(df,steps)
print(result)

