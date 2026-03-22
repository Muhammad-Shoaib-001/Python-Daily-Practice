import pandas as pd
import sqlite3 as sql

df = pd.read_csv("Employee.csv")

df = df.drop_duplicates()
df["Education"] = df["Education"].str.replace("Bachelors","BA")
df["Education"] = df["Education"].str.replace("Masters","MA")
df["Gender"] = df["Gender"].str.strip().map({"Male":'M',"Female":'F'})
df.columns = df.columns.str.replace(" ","_").str.capitalize()

conn = sql.connect("employees.db")
df.to_sql("employees", conn, if_exists="replace", index=False)
cursor = conn.cursor()
cursor.execute("SELECT Gender FROM employees LIMIT 5")
print(cursor.fetchall())
conn.close()