import sqlite3

# Connect to your SQLite database (create if  it doesn't exist)
conn = sqlite3.connect("mydatabase.db")

# Create the table using your schema
conn.execute("""
    CREATE TABLE agent (
        time TEXT,
        assignedAgentId TEXT,
        targetSkillId INTEGER,  -- Note: Long changed to INTEGER 
        targetSkillName TEXT,
        reason TEXT,
        by TEXT,
        sourceSkillId INTEGER,  -- Note: Long changed to INTEGER
        sourceSkillName TEXT,
        sourceAgentId TEXT,
        sourceAgentFullName TEXT,
        sourceAgentLoginName TEXT,
        sourceAgentNickname  TEXT, 
        dialogId TEXT
    );
""")

conn.commit()  # Save the changes
print("Table 'agent' created successfully!")

sample_data = [
    (
        "2023-11-19 10:22:11.123456",  # BigQuery Datetime format
        "1234",
        5678,
        "Customer Service",
        "SuggestedAgentTimeout",
        '5678',
        9012,
        "Sales",
        "9012",
        "John Doe",
        "jdoe",
        "1234",  # For sourceAgentNickname
        "123456"
    ),

]

# Insert data into the table
conn.executemany("""
    INSERT INTO agent VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", sample_data)

conn.commit()  # Save the changes
print("Sample data inserted!")