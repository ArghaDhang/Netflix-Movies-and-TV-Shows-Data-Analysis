# Import the necessary libraries-step1
import pandas as pd
import matplotlib.pyplot as plt

# Load the Netflix dataset-step2

df=pd.read_csv('netflix_titles.csv')
# print(df.head())

# clean Data
df=df.dropna(subset=['type','country','rating','duration','release_year'])

# Line_chart--->
type_count=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index,type_count.values,color=['skyblue','orange'])
plt.title("Number of Movies and TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('netflix_type_count.png',dpi=300,bbox_inches='tight')
plt.show()

# # Pie chart--->
rating_count=df['rating'].value_counts().head()
plt.figure(figsize=(8,6))
plt.pie(rating_count,labels=rating_count.index,autopct='%1.1f%%',startangle=90)
plt.title("Percentage of content rating on Netflix")
plt.xlabel("Type")
plt.ylabel("Count") 
plt.tight_layout()
plt.savefig('content_rating_pie.png',dpi=300,bbox_inches='tight')
plt.show()

# # Histogram chart--->
movie_df=df[df['type']=='Movie'].copy()
movie_df['duration']=movie_df['duration'].str.replace(' min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie_df['duration'],bins=30,color='purple',edgecolor='black')
plt.title("Distribution of Movie Durations on Netflix")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig('movie_duration_histogram.png',dpi=300,bbox_inches='tight')
plt.show()

# Scatter plot--->
realse_count=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(realse_count.index,realse_count.values,color='red',marker='o')
plt.title("Number of Movies and TV Shows Released Over the Years on Netflix")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('release_year_scatter.png',dpi=300,bbox_inches='tight')
plt.grid()
plt.show()

# Bar chart
country_count=df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values,color='teal')
plt.title("Top 10 Countries by Number of Titles on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig('top_countries_barh.png',dpi=300,bbox_inches='tight')
plt.show()

# Group by both release_year and type
content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# First subplot: Movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue', label='Movies')
ax[0].set_title("Movies Released Over the Years")
ax[0].set_xlabel("Release Year")
ax[0].set_ylabel("Number of Movies")
ax[0].legend()

# Second subplot: TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange', label='TV Shows')
ax[1].set_title("TV Shows Released Over the Years")
ax[1].set_xlabel("Release Year")
ax[1].set_ylabel("Number of TV Shows")
ax[1].legend()

# Add overall title and layout settings
fig.suptitle('Comparison of Movies and TV Shows Released Over the Years on Netflix')
plt.tight_layout()
plt.savefig('movies_tvshows_comparison.png', dpi=300, bbox_inches='tight')
plt.show()