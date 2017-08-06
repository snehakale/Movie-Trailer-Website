## Project Title 
### Movie Trailer Website

This is a _movie trailer website_. This project produces a web page which shows different movies along with thier poster images. If user clicks on any movie, the trailer of that movie will be played.

## Pre-requisites 
1. Download [Python](https://www.python.org/downloads/)
2. Download the python files from the given github repository.  

## Installation
1. Install `python` on your machine and set the path variable.
   You can refer the step-by-step installation for python on _Windows_ [here](https://www.howtogeek.com/197947/how-to-install-python-on-windows/)  
   and for _Mac_ you can refer [here](https://docs.python.org/3/using/mac.html)
 2. Download /Unzip the files viz. `media.py`,`entertainment_center.py` and `fresh_tomatoes.py` and keep them all in a same folder.
  3.  Run `entertain_center.py` file to get the output.
  4. Click on any movie to watch it's trailer.

## Code Example
This project mainly has 3 python files. 
1. In `media.py`, there is a definition for class `Movie`, which includes `__init__()` method to initialize the instance variables 
   `def __init__(self, movie_title,,----):
   self.title = movie_title ...... `

   and `show_trailer()` method to play the trailer for selected movie by opening it's _youtube URL_.
`def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)`

2. In `entertainment_center.py`, few instances of class Movie are created.
`spiderman_homecoming = media.Movie("Spider-Man: Homecoming",
                                   "Thrilled by his experience with the Avengers, Spiderman returns home to live with his Aunt May.",
                                   ---)`
                                   
    Ths list of those instances is created and passed as an argument for `open_movies_page(movies)` method of `fresh_tomatoes.py` file.

   `movies = [spiderman_homecoming, girls...]` 
   `fresh_tomatoes.open_movies_page(movies)`
   

3. `fresh_tomatoes.py` creates a layout page to show the movies along with their poster images in a specified format and provides a functionality to play the trailer of a movie being selected.
`def open_movies_page(movies):`


## Test
Simple tests for this web page can be done as follows :
- Check whether the movies are properly formatted along with their names and poster images.
- Select any movie and check whether it's trailer is getting played or not.

## Reference 
Refer [Python 3.2 documentation](https://docs.python.org/3.2/py-modindex.html#) for modules webbroswer,os,re 
## Author
Sneha Kale
 



