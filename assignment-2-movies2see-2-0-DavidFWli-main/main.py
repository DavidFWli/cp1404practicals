from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from movie import Movie
from moviecollection import MovieCollection
import json

Builder.load_file('app.kv')
MOVIES_FILE = "movies.json"

class MovieApp(App):
    def build(self):
        self.title = "Movies2See 2.0 - by LIHEWEI"

        self.movie_collection = MovieCollection(filename=MOVIES_FILE)
        self.movie_collection.load_movies()

        layout = BoxLayout(orientation='vertical', padding=10)

        sort_layout = self.create_sort_layout()
        layout.add_widget(sort_layout)

        grid_layout = BoxLayout(orientation='horizontal', spacing=10)
        left_layout = self.create_left_layout()
        right_layout = self.create_right_layout()

        grid_layout.add_widget(left_layout)
        grid_layout.add_widget(right_layout)

        layout.add_widget(grid_layout)
        self.display_movies()
        return layout

    def create_sort_layout(self):
        sort_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='48dp', spacing=10)
        sort_label = Label(text='Sort:', size_hint=(None, None), size=('100dp', '48dp'), halign='center',
                           valign='middle')

        sort_layout.add_widget(sort_label)
        self.movie_count_label = Label(text=self.get_movie_count_text())
        sort_layout.add_widget(self.movie_count_label)
        return sort_layout

    def create_left_layout(self):
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
        return left_layout

    def create_right_layout(self):
        right_layout = BoxLayout(orientation='vertical', spacing=5, size_hint=(0.75, 1))
        scroll_view = ScrollView()
        self.movies_layout = BoxLayout(orientation='vertical', spacing=5, padding=10)
        scroll_view.add_widget(self.movies_layout)
        right_layout.add_widget(scroll_view)

        bottom_right_layout = BoxLayout(size_hint=(None, None), size=(right_layout.width, '30dp'),
                                        pos_hint={'right': 0.5, 'bottom': 1, 'left': 0.5})
        welcome_label = Label(text='Welcome to Movie2see :)', size_hint=(None, None), size=('100dp', '30dp'),
                              halign='center', valign='middle')
        bottom_right_layout.add_widget(welcome_label)
        right_layout.add_widget(bottom_right_layout)
        return right_layout

    def display_movies(self):
        self.movies_layout.clear_widgets()
        for movie_data in self.movie_collection.movies:
            watched_status = " watched" if movie_data.status else ""
            button_text = f"{movie_data.title} - ({movie_data.category} {movie_data.year}){watched_status}"
            button = Button(text=button_text, size_hint_y=None, height='90dp')

            if movie_data.status:
                button.background_color = (88, 88, 0, 0.5)  # Watched movie color
            else:
                button.background_color = (0, 88, 88, 0.5)  # Unwatched movie color

            self.movies_layout.add_widget(button)

    def get_movie_count_text(self):
        unwatched_count = sum(1 for movie in self.movie_collection.movies if not movie.status)
        watched_count = sum(1 for movie in self.movie_collection.movies if movie.status)
        return f"Movies to Watch: {unwatched_count} | Movies Watched: {watched_count}"

    def add_movie(self, instance):
        title = self.title_input.text.strip()
        year = self.year_input.text.strip()
        category = self.category_input.text.strip()
        watched = self.root.ids.watched_checkbox.active

        if title and year and category:
            new_movie = Movie(title, year, category, watched)
            self.movie_collection.add_movie(new_movie)
            self.display_movies()
            self.movie_count_label.text = self.get_movie_count_text()
            self.movie_collection.save_movies()
            self.root.ids.scroll_view.scroll_to(self.movies_layout.children[0])

            for button in self.movies_layout.children:
                if button.text.startswith(f"{new_movie.title}"):
                    button.bind(on_press=lambda instance: self.mark_as_watched(new_movie, button))

    def mark_as_watched(self, movie, button):
        movie.status = "true"
        button.background_color = (88, 88, 0, 0.5)
        self.movie_collection.save_movies()
        self.movie_count_label.text = self.get_movie_count_text()

    def clear_inputs(self, instance):
        self.title_input.text = ''
        self.year_input.text = ''
        self.category_input.text = ''


if __name__ == '__main__':
    MovieApp().run()
