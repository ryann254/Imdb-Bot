import imdb

movie_name = input('Which movies or series would you like to search for: ')
moviesDB = imdb.IMDb()

movies = moviesDB.search_movie(movie_name)
id = movies[0].getID()
movie = moviesDB.get_movie(id)
title = movie['title']
year = movie['year']
rating = movie['rating']
directors = movie['directors']
casting = movie['cast']

print('Print movie info: ')
print('{} - {}'.format(title,year))
print('rating - {}'.format(rating))
directorsStr = ' '.join(map(str, directors))
print('directors - {}'.format(directorsStr))
actors = ', '.join(map(str, casting))
print('actors - {}'.format(actors))