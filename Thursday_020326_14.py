import os
import sqlite3 as sql
import pandas as pd

try:
    df = pd.read_csv('Employee.csv')
except:     
    print('No file found')

def clean(df):
    df = df.drop_duplicates().copy()
    df.columns = (df.columns.str.replace(r'(?<!^)(?=[A-Z])', '_', regex=True))
    df.loc[:,"Gender"] = (
        df["Gender"].str.
        strip().replace({"Male":"M","Female":"F"})
    )
    df.loc[:,"Education"] = (
        df["Education"].str.
        strip().replace({"Bachelors":"BA","Masters":"MA"})
    )
    df.loc[:,"Payment_Tier"] = (
        pd.to_numeric(df["Payment_Tier"],errors="coerce")
    )
    df.loc[:,"City"] = df["City"].fillna("Unknown")
    return df

def load(df):
    if os.path.exists("employees.db"):
        os.remove("employees.db")
    conn = sql.connect("employees.db")
    df.to_sql("Employees",conn,if_exists="replace",index=False)
    return conn

def validate(conn, query="SELECT * FROM Employees"):
    # result = pd.read_sql(query,conn)
    # return result
    cursor = conn.cursor()
    result = cursor.execute(query)
    return result.fetchall()


def pipeline_runner(df, steps):
    clean_df = None
    conn = None
    result = None

    for step in steps:
        if step == clean:
            clean_df = step(df)

        elif step == load:
            if clean_df is not None:
                conn = step(clean_df)
            else:
                conn = step(df)

        elif step == validate:
            if conn is not None:
                result = step(conn)
            else:
                print("No connection available")

    if result is not None:
        return result
    elif conn is not None:
        return conn
    elif clean_df is not None:
        return clean_df
    else:
        return df
    
steps = [clean,load,validate]
result = pipeline_runner(df,steps)
print(result)
         
