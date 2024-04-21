from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import csv

MOVIES_FILE = "movies.csv"
UNWATCHED = "u"
WATCHED = "w"


class MovieApp(App):

    def build(self):
        self.title = "Movies2See 2.0 - by LIHEWEI"
        self.movies = self.load_movies()

        layout = BoxLayout(orientation='vertical', padding=10)

        # Sort Layout
        sort_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='48dp', spacing=10)
        sort_label = Label(text='Sort:', size_hint=(None, None), size=('100dp', '48dp'),
                           halign='center', valign='middle')

        sort_layout.add_widget(sort_label)
        self.movie_count_label = Label(text=self.get_movie_count_text())
        sort_layout.add_widget(self.movie_count_label)
        layout.add_widget(sort_layout)

        # Main Layout
        grid_layout = BoxLayout(orientation='horizontal', spacing=10)

        # Left Layout
        left_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.25, 1))

        category_button = Button(text='Category', size_hint_y=None, height='48dp')
        category_button.bind(on_press=self.add_movie)
        left_layout.add_widget(category_button)

        left_layout.add_widget(Label(text='Title:'))
        self.title_input = TextInput(multiline=False)
        left_layout.add_widget(self.title_input)
        left_layout.add_widget(Label(text='Year:'))
        self.year_input = TextInput(input_type='number')
        left_layout.add_widget(self.year_input)
        left_layout.add_widget(Label(text='Category:'))
        self.category_input = TextInput(multiline=False)
        left_layout.add_widget(self.category_input)

        add_button = Button(text='Add Movie', size_hint_y=None, height='48dp')
        add_button.bind(on_press=self.add_movie)
        left_layout.add_widget(add_button)

        clear_button = Button(text='Clear', size_hint_y=None, height='48dp')
        clear_button.bind(on_press=self.clear_inputs)
        left_layout.add_widget(clear_button)

        grid_layout.add_widget(left_layout)

        # Right Layout
        right_layout = BoxLayout(orientation='vertical', spacing=5, size_hint=(0.75, 1))

        # Scroll View for movies
        scroll_view = ScrollView()
        self.movies_layout = BoxLayout(orientation='vertical', spacing=5, padding=10)
        scroll_view.add_widget(self.movies_layout)
        right_layout.add_widget(scroll_view)

        bottom_right_layout = BoxLayout(size_hint=(None, None), size=(layout.width, '30dp'),
                                        pos_hint={'right': 0.5, 'bottom': 1, 'left': 0.5})
        welcome_label = Label(text='Welcome to Movie2see :)', size_hint=(None, None), size=('100dp', '30dp'),
                              halign='center', valign='middle')
        bottom_right_layout.add_widget(welcome_label)
        right_layout.add_widget(bottom_right_layout)

        grid_layout.add_widget(right_layout)

        layout.add_widget(grid_layout)

        self.display_movies()

        return layout

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
        self.movies_layout.clear_widgets()

        for movie in self.movies:
            button = Button(text=f"{movie[0]} - {movie[2]} ({movie[1]})", size_hint_y=None, height='90dp')
            button.background_color = (0, 88, 88, 0.5) if movie[3] == UNWATCHED else (88, 88, 0, 0.5)
            self.movies_layout.add_widget(button)

    def add_movie(self, instance):
        title = self.title_input.text.strip()
        year = self.year_input.text.strip()
        category = self.category_input.text.strip()

        if title and year and category:
            self.movies.insert(0, [title, year, category, UNWATCHED])
            self.display_movies()
            self.save_movies()

    def clear_inputs(self, instance):
        self.title_input.text = ''
        self.year_input.text = ''
        self.category_input.text = ''

    def get_movie_count_text(self):
        unwatched_count = len([movie for movie in self.movies if movie[3] == UNWATCHED])
        watched_count = len([movie for movie in self.movies if movie[3] == WATCHED])
        return f"Movies to Watch: {unwatched_count} | Movies Watched: {watched_count}"


if __name__ == '__main__':
    MovieApp().run()
