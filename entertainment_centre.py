import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Movie about a boy, where his toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Movie about Avatars",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
