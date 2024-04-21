import json
from movie import Movie

class MovieCollection:
    def __init__(self, filename="movies.json"):
        self.movies = []
        self.filename = filename

    def load_movies(self):
        try:
            with open(self.filename, "r") as file:
                movies_data = json.load(file)
                for movie in movies_data:
                    title = movie.get('title')
                    year = movie.get('year')
                    category = movie.get('category')
                    status = movie.get('is_watched')  # Corrected to 'is_watched'
                    self.movies.append(Movie(title, year, category, status))
        except FileNotFoundError:
            print("File not found")

    def save_movies(self):
        movies_data = []
        for movie in self.movies:
            movies_data.append({
                'title': movie.title,
                'year': movie.year,
                'category': movie.category,
                'is_watched': movie.status  # Save True or False, not "watched" or "unwatched"
            })
        with open(self.filename, "w") as file:
            json.dump(movies_data, file, indent=4)

    def add_movie(self, movie):
        self.movies.append(movie)

    def sort(self, key):
        self.movies.sort(key=lambda x: getattr(x, key))

    def __str__(self):
        movie_list = "\n".join(str(movie) for movie in self.movies)
        return f"Movies:\n{movie_list}"

def run_movie_collection():
    """Load, manipulate, and save movies using MovieCollection class."""

    # Load movies from file
    movie_collection = MovieCollection()
    movie_collection.load_movies()

    # Display loaded movies
    print("Loaded movies:")
    print(movie_collection)

    # Sort movies by title and display
    print("Sorted movies by title:")
    movie_collection.sort("title")
    print(movie_collection)

    # Save movies to file (optional, only save when needed)
    # movie_collection.save_movies()
    # print("Movies saved.")

# Only run the function if this script is executed directly, not imported
if __name__ == "__main__":
    run_movie_collection()