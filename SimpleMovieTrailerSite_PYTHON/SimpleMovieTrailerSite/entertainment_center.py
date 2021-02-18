"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

def main():
    """Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer link and release date."""
    cm = media.Movie("Captain Marvel",
                          "MCU's most powerful superhero",
                          "https://stat.ameba.jp/user_images/20190108/19/jumbooomori/68/06/j/o0821120014335603368.jpg?caw=800",
                          "https://www.youtube.com/watch?v=0LHxvxdRnYc",
                          "March 8, 2019")

    ae = media.Movie("Avengers: EndGame",
                          "The Avengers take a final stand against Thanos",
                          "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_.jpg",
                          "https://www.youtube.com/watch?v=TcMBFSGVi1c",
                          "April 26, 2019")

    sm = media.Movie("Spider-Man: FFH",
                           "Following the events of Avengers: Endgame,",
                           "https://terrigen-cdn-dev.marvel.com/content/prod/1x/sffh_venice-high-res.jpg",
                           "https://www.youtube.com/watch?v=Nt9L1jCKGnE",
                           "July 5, 2019")

    xm = media.Movie("X-Men: Dark Phoenix",
                         "Jean Grey begins to develop incredible powers",
                         "https://m.media-amazon.com/images/M/MV5BMjAwNDgxNTI0M15BMl5BanBnXkFtZTgwNTY4MDI1NzM@._V1_.jpg",
                         "https://www.youtube.com/watch?v=azvR__GRQic",
                         "June 7, 2019")

    sz = media.Movie("Shazam!",
                           "An effortlessly entertaining blend of humor and heart",
                           "https://m.media-amazon.com/images/M/MV5BYTE0Yjc1NzUtMjFjMC00Y2I3LTg3NGYtNGRlMGJhYThjMTJmXkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_.jpg",
                           "https://www.youtube.com/watch?v=uilJZZ_iVwY",
                           "April 5, 2019")

    ach = media.Movie("Annabelle Comes Home",
                          "Determined to keep Annabelle from wreaking more havoc",
                          "https://m.media-amazon.com/images/M/MV5BYmI4NDNiMmQtZTFkYi00ZDVmLThlYTAtMWJlMjU1M2I2ZmViXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=EMa-KFfatT0",
                          "June 26, 2019")

    # Store the Movie objects in a list.
    movies = [cm, ae, sm, xm, sz, ach]

    # Open the movie website in the user's browser, featuring the movies above.
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
