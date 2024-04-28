"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
LI HEWEI, first version: 11/07/2016
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = ["Alice", "Bob", "Charlie", "David"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        return Builder.load_file('dynamic_labels.kv')

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        layout = self.root.ids.main
        layout.clear_widgets()  # Clear any existing labels before creating new ones
        for name in self.names:
            label = Label(text=name)
            layout.add_widget(label)


if __name__ == "__main__":
    DynamicLabelsApp().run()