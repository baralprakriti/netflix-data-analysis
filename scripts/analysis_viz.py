import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# 1. Connect to your database
engine = create_engine('mysql+mysqlconnector://root:123@localhost/netflix_db')

# 2. Pull the data
df = pd.read_sql("SELECT type, release_year, date_added FROM netflix_titles", engine)

# 3. Clean the 'date_added' column
# We need to turn the text "September 25, 2021" into a real Python date
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year

# 4. Filter out any years that look like errors (e.g., before Netflix streaming started)
df_filtered = df[df['year_added'] > 2008]

# 5. Create the Visualization
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid") # Makes it look modern

# Use a countplot to show Movies vs TV Shows added each year
sns.countplot(data=df_filtered, x='year_added', hue='type', palette='viridis')

plt.title('The Evolution of Netflix Content: Movies vs TV Shows', fontsize=16)
plt.xlabel('Year Content was Added to Netflix', fontsize=12)
plt.ylabel('Count of Titles', fontsize=12)
plt.legend(title='Content Type')

# 6. Save the insight
plt.savefig('netflix_trend.png')
print("✅ Chart saved as 'netflix_trend.png'. Open it in your folder!")