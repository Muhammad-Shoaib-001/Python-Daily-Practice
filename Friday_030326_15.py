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
        df["Gender"].str.strip().replace({"Male":"M","Female":"F"})
    )
    df.loc[:,"Education"] = (
        df["Education"].str.strip().replace({"Bachelors":"BA","Masters":"MA"})
    )
    df.loc[:,"Payment_Tier"] = (
        pd.to_numeric(df["Payment_Tier"],errors="coerce")
    )
    df.loc[:,"City"] = df["City"].fillna("Unknown")
    return df

def batch(data,process):
    batch = []
    batch_size = 500
    for row in data:
        batch.append(row)

        if len(batch) >= batch_size:
            process(batch)
            print(f"Processed batch of size {batch_size}")

            batch.clear()
            if batch_size < 5000:
                batch_size += 500

    # remaining data
    if batch:
        process(batch)

def load(df):
    if os.path.exists("employees.db"):
        os.remove("employees.db")
    conn = sql.connect("employees.db")
    cursor = conn.cursor()
    columns = df.columns
    columns_sql = ", ".join([f"{col} TEXT" for col in columns])
    cursor.execute(f"CREATE TABLE Employees ({columns_sql})")
    placeholders = ", ".join(["?"] * len(columns))
    total_inserted = 0 
    batch_number = 1
   
    def process(batch_data):
        nonlocal batch_number,total_inserted
        cursor.executemany( f"INSERT INTO Employees VALUES ({placeholders})",batch_data)
        conn.commit()
        batch_size_current = len(batch_data)
        total_inserted += batch_size_current
        print(f"Batch: {batch_number} inserted: {batch_size_current} rows | Total: {total_inserted} ")
       
  # 🔹 convert dataframe → rows
    data = df.itertuples(index=False, name=None)

    # 🔹 use batching
    batch(data, process)

    return conn

def validate(conn, query="SELECT count(*) FROM Employees"):
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
         
