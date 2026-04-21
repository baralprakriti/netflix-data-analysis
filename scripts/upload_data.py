import pandas as pd
from sqlalchemy import create_engine
import os

# 1. Path Checker - This helps us find the file
file_name = 'netflix_titles.csv' # Change to 'data/netflix_titles.csv' if it's in a folder

if os.path.exists(file_name):
    print(f"✅ Found {file_name}!")
else:
    print(f"❌ Cannot find {file_name} in the current folder.")
    print(f"Current folder contents: {os.listdir('.')}")

# 2. Load the CSV
try:
    df = pd.read_csv(file_name, encoding='latin1')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    print("✅ CSV loaded successfully!")
    
    # 3. Connection Settings
    USER = 'root'
    PASSWORD = 'your_password' 
    HOST = 'localhost'
    DATABASE = 'netflix_db'

    # 4. Upload to MySQL
    engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}")
    df.to_sql('netflix_titles', engine, if_exists='replace', index=False)
    print("🚀 SUCCESS! Data is now in MySQL.")

except Exception as e:
    print(f"❌ Error: {e}")