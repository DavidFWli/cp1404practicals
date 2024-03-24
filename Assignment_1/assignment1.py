import csv

# Constants
MOVIES_FILE = "Movies2See.csv"
UNWATCHED = "u"
WATCHED = "w"


# Functions
def load_movies():
    try:
        with open(MOVIES_FILE, "r", newline="") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def save_movies(movies):
    with open(MOVIES_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movies)


def display_movies(movies):
    unwatched_count = 0
    for index, movie in enumerate(movies):
        if movie[3] == UNWATCHED:
            print(f"{index}. * {movie[0]} - {movie[2]} ({movie[1]})")
            unwatched_count += 1
        else:
            print(f"{index}. {movie[0]} - {movie[2]} ({movie[1]})")
    print(f"{unwatched_count} movies watched, {len(movies) - unwatched_count} movies still to watch")


def add_movie(movies):
    title = input("Title: ").strip()
    while not title:
        print("Input can not be blank")
        title = input("Title: ").strip()

    year = input("Year: ")
    while not year.isdigit() or int(year) < 0:
        print("Invalid input; enter a valid number")
        year = input("Year: ")

    category = input("Category: ").strip()
    while not category:
        print("Input can not be blank")
        category = input("Category: ").strip()

    movies.append([title, year, category, UNWATCHED])
    print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(movies):
    unwatched_movies = [index for index, movie in enumerate(movies) if movie[3] == UNWATCHED]
    if not unwatched_movies:
        print("No more movies to watch!")
        return

    display_movies(movies)
    try:
        choice = int(input("Enter the number of a movie to mark as watched\n"))
        if choice < 0 or choice >= len(movies):
            print("Invalid movie number")
            return

        if choice in unwatched_movies:
            movies[choice][3] = WATCHED
            print(f"{movies[choice][0]} from {movies[choice][1]} watched")
        else:
            print("You have already watched", movies[choice][0])
    except ValueError:
        print("Invalid input; enter a valid number")


# Main function
def main():
    print("Movies2See 1.0 - by LIHEWEI")
    movies = load_movies()
    print(len(movies), "movies loaded")

    while True:
        print("Menu")
        print("D - Display movies")
        print("A - Add new movie")
        print("W - Watch a movie")
        print("Q - Quit")
        choice = input("~ ").upper()

        if choice == "D":
            display_movies(movies)
        elif choice == "A":
            add_movie(movies)
        elif choice == "W":
            watch_movie(movies)
        elif choice == "Q":
            save_movies(movies)
            print(len(movies), "movies saved to", MOVIES_FILE)
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()
