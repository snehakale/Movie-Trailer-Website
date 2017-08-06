import media  # Importing media to use class Movie
import fresh_tomatoes  # Importing fresh_tomatoes to open a movie website page

# Creating instances of class Movie
spiderman_homecoming = media.Movie("Spider-Man: Homecoming",
                                   "Thrilled by his experience with the Avengers, Spiderman returns home to live with his Aunt May.",
                                   "http://t0.gstatic.com/images?q=tbn:ANd9GcT8W3Fe7DD101g0M7OCalJN9u675sQAJFslGCjvs74PTOfEKt_t",
                                   "https://www.youtube.com/watch?v=OiyeBWwlvsY")

girls_trip = media.Movie("Girls Trip",
                         "Four best friends are in for the adventure of a lifetime when"
                         " they travel to New Orleans for the annual Essence Festival.",
                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNqrxPIcQsbppA4M326MeyPcn5xwUMtGrtz9sWZtexo_7IRnFM",
                         "https://www.youtube.com/watch?v=91moJ3jfXV0")

back_to_the_future = media.Movie("Back To The Future",
                                 "A teen thrown back to 1950s with an experiment by his scientiest friend",
                                 "http://t3.gstatic.com/images?q=tbn:ANd9GcT9d_lBBx0xxB7_d4RP82MlRcK82lzT2W1ZavxhV39SSTZOofDX",
                                 "https://www.youtube.com/watch?v=JWyOC4n4qSc")

midnight_in_paris = media.Movie("Midnight In Paris",
                               "A screenwriter, while vacationing in Paris with his fiancee ,has taken on tour of a city alone",
                               "http://t3.gstatic.com/images?q=tbn:ANd9GcTk3ssys2bKM5-U6XMgvoD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                               "https://www.youtube.com/watch?v=wuOUdZjuCIA")

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to a life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")

# Creating list of movies
movies = [spiderman_homecoming, girls_trip, back_to_the_future, midnight_in_paris, toy_story, avatar]

# Calling a layout page
fresh_tomatoes.open_movies_page(movies)


