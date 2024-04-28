"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
LI HEWEI, IT@JCU
06/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'LI HEWEI'

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    km_output = StringProperty("0.0")

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be triggered by text input change), output result to label widget """
        try:
            value = float(value)
            result = value * MILES_TO_KM
            self.km_output = str(result)
        except ValueError:
            self.km_output = "0.0"

    def handle_increment(self, change):
        """
        handle up/down button press, update the text input with new value, call calculation function
        :param change: the amount to change
        """
        try:
            value = float(self.root.ids.input_miles.text) + change
        except ValueError:
            value = change
        self.root.ids.input_miles.text = str(int(value))
        self.handle_calculate(value)


if __name__ == "__main__":
    MilesConverterApp().run()