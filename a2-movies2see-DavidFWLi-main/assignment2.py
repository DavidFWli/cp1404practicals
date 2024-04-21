from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
import csv

MOVIES_FILE = "movies.csv"
UNWATCHED = "u"
WATCHED = "w"


class MovieApp(App):

    def build(self):
        self.title = "Movies2See 2.0 - by LIHEWEI"
        self.movies = self.load_movies()

        layout = BoxLayout(orientation='vertical', padding=10)

        sort_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='48dp', spacing=10)
        self.movie_count_label = Label(text=f"Movies to Watch: {len([movie for movie in self.movies if movie[3] == UNWATCHED])} | Movies Watched: {len([movie for movie in self.movies if movie[3] == WATCHED])}")
        sort_layout.add_widget(self.movie_count_label)
        layout.add_widget(sort_layout)

        grid_layout = BoxLayout(orientation='horizontal', spacing=10)

        left_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.25, 1))
        add_button = Button(text='Add Movie', size_hint_y=None, height='48dp')
        add_button.bind(on_press=self.add_movie)
        left_layout.add_widget(add_button)

        left_layout.add_widget(Label(text='Title:'))
        self.title_input = TextInput(multiline=False)
        left_layout.add_widget(self.title_input)
        left_layout.add_widget(Label(text='Year:'))
        self.year_input = TextInput(input_type='number')
        left_layout.add_widget(self.year_input)
        left_layout.add_widget(Label(text='Category:'))
        self.category_input = TextInput(multiline=False)
        left_layout.add_widget(self.category_input)

        clear_button = Button(text='Clear', size_hint_y=None, height='48dp')
        clear_button.bind(on_press=self.clear_inputs)
        left_layout.add_widget(clear_button)

        grid_layout.add_widget(left_layout)

        right_layout = BoxLayout(orientation='vertical', spacing=5, size_hint=(0.75, 1))
        scroll_view = ScrollView()
        self.movies_list = BoxLayout(orientation='vertical', spacing=5, padding=10)
        scroll_view.add_widget(self.movies_list)
        right_layout.add_widget(scroll_view)

        watch_button = Button(text='Watch Movie', size_hint_y=None, height='48dp')
        watch_button.bind(on_press=self.watch_movie)
        right_layout.add_widget(watch_button)

        grid_layout.add_widget(right_layout)

        layout.add_widget(grid_layout)

        self.display_movies()

        return layout

    def reset_button_color(self, button):
        button.background_color = get_color_from_hex('#ffffff')

    def load_movies(self):
        try:
            with open(MOVIES_FILE, "r", newline="") as file:
                reader = csv.reader(file)
                movies = list(reader)
                movies.sort(key=lambda x: int(x[1]))
                return movies
        except FileNotFoundError:
            return []

    def save_movies(self):
        with open(MOVIES_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.movies)

    def display_movies(self):
        self.movies_list.clear_widgets()

        for index, movie in enumerate(self.movies):
            button = Button(text=f"{movie[0]} - {movie[2]} ({movie[1]})", size_hint_y=None, height='40dp')
            if movie[3] == UNWATCHED:
                button.background_color = (0, 88, 88, 0.5)
            else:
                button.background_color = (88, 88, 0, 0.5)
            self.movies_list.add_widget(button)

    def add_movie(self, instance):
        title = self.title_input.text.strip()
        year = self.year_input.text.strip()
        category = self.category_input.text.strip()

        if not title or not year or not category:
            return

        self.movies.insert(0, [title, year, category, UNWATCHED])
        self.display_movies()
        self.save_movies()

    def clear_inputs(self, instance):
        self.title_input.text = ''
        self.year_input.text = ''
        self.category_input.text = ''

    def watch_movie(self, instance):
        unwatched_movies = [index for index, movie in enumerate(self.movies) if movie[3] == UNWATCHED]
        if not unwatched_movies:
            return

        movie_to_watch = unwatched_movies[0]
        self.movies[movie_to_watch][3] = WATCHED
        self.display_movies()
        self.save_movies()


if __name__ == '__main__':
    MovieApp().run()