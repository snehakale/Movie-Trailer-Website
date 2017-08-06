import webbrowser  # Importing webbrowser module to use open method

class Movie():
    """
        This is a class Movie.
        It defines some features of the Movie eg. movie title, movie poster image etc.
        Also has a method to show the trailer for a movie.
    """
    
    # Calling a construcor to initialize istance variables    
    def __init__(self, movie_title, movie_storyline, movie_poster_image_url,
                 movie_trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    # A function to show trailer for a movie  
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
