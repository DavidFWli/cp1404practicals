import json
from movie import Movie  # Assuming you have a Movie class defined in movie.py

class MovieCollection:
    def __init__(self):
        self.movies = []

    def load_movies(self, filename):
        try:
            with open(filename, "r") as file:
                movies_data = json.load(file)
                for movie in movies_data:
                    title = movie.get('title')
                    year = movie.get('year')
                    category = movie.get('category')
                    status = movie.get('status')
                    self.movies.append(Movie(title, year, category, status))
        except FileNotFoundError:
            print("File not found")

    def __str__(self):
        movie_list = "\n".join(str(movie) for movie in self.movies)
        return f"Movies:\n{movie_list}"

    def add_movie(self, movie):
        self.movies.append(movie)

    def sort(self, key):
        self.movies.sort(key=lambda x: getattr(x, key))

    def save_movies(self, filename):
        movies_data = []
        for movie in self.movies:
            movies_data.append({
                'title': movie.title,
                'year': movie.year,
                'category': movie.category,
                'status': movie.status
            })
        with open(filename, "w") as file:
            json.dump(movies_data, file, indent=4)

    def test_sorting(self):
        print("Test sorting - title:")
        self.sort("title")
        print(self)
        print("Test sorting - year:")
        self.sort("year")
        print(self)
        print("Test sorting - category:")
        self.sort("category")
        print(self)
        print("Test sorting - status:")
        self.sort("status")
        print(self)

def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # An empty list is considered False

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies("movies.json")
    print(movie_collection)
    assert movie_collection.movies  # Assuming file is non-empty; non-empty list is considered True

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_collection)

    # Test sorting movies
    movie_collection.test_sorting()

    # Test saving movies
    print("Test saving movies:")
    movie_collection.save_movies("output.json")
    print("Movies saved.")

    # TODO: Add more tests, as appropriate, for each method


run_tests()
