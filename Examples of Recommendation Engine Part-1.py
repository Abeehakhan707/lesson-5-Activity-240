import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

data = pd.read_csv('ratings.csv')
data.head(10)

movies_data = pd.read_csv('movies.csv')
movies_data.head(10)

data = data.merge(movies_data, on='movieId', how = 'left')
data.head()

movies_data['year'] = movies_data.title.str.extract('(\(\d\d\d\d\))', expand=True) 
movies_data['year'] = movies_data.year.str.extract('(\d\d\d\d)', expand=True)
movies_data.head()

movies_data['title'] = movies_data.title.str.replace('(\(\d\d\d\d\))', '')
movies_data['title'] = movies_data['title'].apply(lambda x: x.strip())
movies_data.head()

movies_data['genres'] = movies_data.genres.str.split('|')
movies_data.head()

movies_copy = movies_data.copy()
for index, row in movies_copy.iterrows():
    for genre in row['genres']:
        movies_copy.at[index, genre] = 1
movies_copy = movies_copy.fillna(0)
movies_copy.head()


data = data.drop(['timestamp'], axis=1)
genre_column = movies_copy.drop(['movieId', 'title', 'genres', 'year'], axis=1)
genre_counts = genre_column.sum(axis = 0)
genre_counts = genre_counts.sort_values(ascending=False)
genre_counts.head()

plt.figure(figsize=(12,10))
plt.bar(genre_counts.index, genre_counts.values)
plt.xlabel('Genres')
plt.ylabel('Count')
plt.title('Distribution of Genres')
plt.xticks(rotation=90)
plt.show()
