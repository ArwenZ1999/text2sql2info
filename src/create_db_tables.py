
import os
import sqlite3
import csv

def create_tables_from_schemas(schemas_folder_path):
    for filename in os.listdir(schemas_folder_path):
        table_name = os.path.splitext(filename)[0]
        with open(os.path.join(schemas_folder_path, filename)) as f:
            reader = csv.reader(f)
            header = next(reader)
            columns = []
            for row in reader:
                columns.append(f"{row[0]} {row[1]}") 
            query = f"CREATE TABLE {table_name} ({', '.join(columns)});"  
        conn.execute(query)
    conn.commit()


if __name__ == "__main__":
  conn = sqlite3.connect("ConversationHistoryRecords.db")
  create_tables_from_schemas("schemas")
