# movie.py
class Movie:
    def __init__(self, title, year, category, status):
        self.title = title
        self.year = year
        self.category = category
        self.status = status
        self.selected = False

    def toggle_status(self):
        self.status = not self.status

    def toggle_selected(self):
        self.selected = not self.selected

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.category} [{'Watched' if self.status else 'Not Watched'}]"
