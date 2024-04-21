class Movie:
    def __init__(self, title, year, category, status):
        self.title = title
        self.year = year
        self.category = category
        self.status = status  # Initialize as True or False, not "true" or "false"

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.category} [{'Watched' if self.status else 'Not Watched'}]"
