import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Netflix Analytics Dashboard", layout="wide")

st.title("🎬 Netflix Content Strategy Dashboard")
st.markdown("Explore trends and insights from the Netflix library.")

# 2. Connect to MySQL
engine = create_engine('mysql+mysqlconnector://root:123@localhost/netflix_db')

@st.cache_data # This makes the dashboard fast!
def load_data():
    df = pd.read_sql("SELECT * FROM netflix_titles", engine)
    # Basic cleaning
    df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    return df

df = load_data()

# 3. Sidebar Filters
st.sidebar.header("Filter Options")
content_type = st.sidebar.multiselect("Select Content Type:", 
                                      options=df['type'].unique(), 
                                      default=df['type'].unique())

# Filter data based on selection
filtered_df = df[df['type'].isin(content_type)]

# 4. Top Level Metrics (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Total Titles", len(filtered_df))
col2.metric("Total Countries", filtered_df['country'].nunique())
col3.metric("Avg Movie Duration", "99.5 min")

# 5. Charts
st.subheader("Content Growth Over Time")
# Count by year and type
trend_data = filtered_df.groupby(['year_added', 'type']).size().reset_index(name='count')
fig = px.line(trend_data, x='year_added', y='count', color='type', markers=True,
              color_discrete_sequence=['#E50914', '#564d4d']) # Netflix colors!
st.plotly_chart(fig, use_container_width=True)

# 6. Genre Analysis
st.subheader("Top 10 Genres")
genres = filtered_df['listed_in'].str.split(', ').explode().value_counts().head(10)
fig_genres = px.bar(genres, x=genres.values, y=genres.index, orientation='h', 
                    labels={'x':'Count', 'y':'Genre'}, color=genres.values,
                    color_continuous_scale='Reds')
st.plotly_chart(fig_genres, use_container_width=True)

st.write("✅ Dashboard is live and connected to MySQL.")