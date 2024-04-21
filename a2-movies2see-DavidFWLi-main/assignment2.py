from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
import csv

MOVIES_FILE = "movies.csv"
UNWATCHED = "u"
WATCHED = "w"

class MovieApp(App):
    def build(self):
        self.title = "Movies2See 2.0 - by LIHEWEI"
        self.movies = self.load_movies()

        layout = BoxLayout(orientation='vertical', padding=10)

        grid_layout = BoxLayout(orientation='horizontal', spacing=10)

        left_layout = BoxLayout(orientation='vertical', spacing=10)
        add_button = Button(text='Add Movie', size_hint_y=None, height='48dp')
        add_button.bind(on_press=self.show_add_movie_popup)
        left_layout.add_widget(add_button)

        left_layout.add_widget(Label(text='Title:'))
        title_input = TextInput(multiline=False)
        left_layout.add_widget(title_input)
        left_layout.add_widget(Label(text='Year:'))
        year_input = TextInput(input_type='number')
        left_layout.add_widget(year_input)
        left_layout.add_widget(Label(text='Category:'))
        category_input = TextInput(multiline=False)
        left_layout.add_widget(category_input)

        grid_layout.add_widget(left_layout)

        right_layout = BoxLayout(orientation='vertical', spacing=5)
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
            label_text = f"{movie[0]} - {movie[2]} ({movie[1]})"
            watched_status = movie[3]
            label = MovieLabel(text=label_text, watched_status=watched_status)
            self.movies_list.add_widget(label)

    def show_add_movie_popup(self, instance):
        popup_layout = BoxLayout(orientation='vertical')

        title_input = TextInput(multiline=False)
        year_input = TextInput(input_type='number')
        category_input = TextInput(multiline=False)

        popup_layout.add_widget(Label(text='Title:'))
        popup_layout.add_widget(title_input)
        popup_layout.add_widget(Label(text='Year:'))
        popup_layout.add_widget(year_input)
        popup_layout.add_widget(Label(text='Category:'))
        popup_layout.add_widget(category_input)

        add_button = Button(text='Add', size_hint_y=None, height='48dp')
        add_button.bind(on_press=lambda instance: self.add_movie_to_list(title_input.text, year_input.text, category_input.text))
        popup_layout.add_widget(add_button)

        self.popup = Popup(title='Add Movie', content=popup_layout, size_hint=(None, None), size=(400, 300))
        self.popup.open()

    def add_movie_to_list(self, title, year, category):
        if not title or not year or not category:
            return

        self.movies.insert(0, [title, year, category, UNWATCHED])
        self.display_movies()
        self.save_movies()
        self.popup.dismiss()

    def watch_movie(self, instance):
        unwatched_movies = [index for index, movie in enumerate(self.movies) if movie[3] == UNWATCHED]
        if not unwatched_movies:
            return

        movie_to_watch = unwatched_movies[0]
        self.movies[movie_to_watch][3] = WATCHED
        self.display_movies()
        self.save_movies()

class MovieLabel(Label):
    watched_status = StringProperty()

if __name__ == '__main__':
    MovieApp().run()