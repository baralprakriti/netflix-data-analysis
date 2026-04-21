import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Setup
engine = create_engine('mysql+mysqlconnector://root:123@localhost/netflix_db')

print("Starting Advanced Analysis...")

# --- TASK 1: GENRE ANALYSIS ---
df_genres = pd.read_sql("SELECT listed_in FROM netflix_titles", engine)
top_genres = df_genres['listed_in'].str.split(', ').explode().value_counts().head(10)

# Visualize the genres
plt.figure(figsize=(10, 6))
top_genres.plot(kind='barh', color='skyblue')
plt.title('Top 10 Most Frequent Genres')
plt.gca().invert_yaxis() # Highest at the top
plt.tight_layout()
plt.savefig('top_genres.png')

# --- TASK 2: DURATION ANALYSIS ---
df_movies = pd.read_sql("SELECT duration FROM netflix_titles WHERE type = 'Movie'", engine)
# Clean and convert
df_movies['duration'] = df_movies['duration'].str.replace(' min', '').astype(float)
avg_duration = df_movies['duration'].mean()

print("\nRESULTS:")
print(f"1. Top Genre: {top_genres.index[0]} with {top_genres.values[0]} titles.")
print(f"2. Average Movie Duration: {avg_duration:.2f} minutes.")
print("3. Chart saved as 'top_genres.png'")