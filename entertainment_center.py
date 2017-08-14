import media  # Importing media to use class Movie
import fresh_tomatoes  # Importing fresh_tomatoes to open a movie website page
import csv  # Importing csv module for csv file reading
import os  # Importing os module

# creating a list of movies
movies = []

# Fetching records from csv file
csvfile = open(os.getcwd()+"\data.csv")
data = csv.reader(csvfile, delimiter=',', quotechar='"')

# Creating a list of movies with each record
for record in data:
    movies.append(media.Movie(record[0], record[1], record[2], record[3]))

# Closing the csv file after using it
csvfile.close()

# Calling a layout page
fresh_tomatoes.open_movies_page(movies)
