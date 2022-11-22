import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.image import Image, AsyncImage
from kivy.cache import Cache
from kivy.lang import Builder
from parse_cards import searchQ, temp_sch


class MainScreen(GridLayout):
    """Class for the main screen"""
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.name = "main_screen"
        # Cache.register("user_input_cache", limit=10, timeout=20)
        self.cols = 1 # screen will have 1 column
        self.search = TextInput(multiline=False) # text input box
        self.submit = Button(text="submit", font_size=30) # button that says submit
        self.submit.bind(on_press=self.switch) # runs switch method when pressed

        # self.search.bind(on_text_validate=self.switch)
        self.add_widget(self.search) # add widgets to screen
        self.add_widget(self.submit)

    def switch(self, instance):
        user_input = self.search.text # gets text from the search box
        search_r = temp_sch(user_input) # runs temp_sch from parse_cards
        njh_app.write_to_result_screen(search_r) # writes results in MyApp class
        njh_app.screen_manager.current = "Result" # move to result screen


class ResultScreen(GridLayout):
    """Class for the result screen (widgets are added in the main MyApp class)"""
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)

    def switch(self, item):
        pass


class MyApp(App):
    def build(self): # this method is where all the widgets are added
        self.screen_manager = ScreenManager() # screen manager allows the use of multiple screens
        # registering and naming screens #
        self.main_screen = MainScreen()
        screen = Screen(name="Main")
        screen.add_widget(self.main_screen) # add screen to main screen
        self.screen_manager.add_widget(screen) # add main screen to screen manager
        self.result_screen = ResultScreen()
        screen = Screen(name="Result")
        screen.add_widget(self.result_screen) # add screen to result screen
        self.screen_manager.add_widget(screen) # add result screen to screen manager
        return self.screen_manager # shows screen manager (with its screens) on app

    def write_to_result_screen(self, text):
        """method to allow dynamic search data to appear on result screen"""
        self.result_screen.cols = 5 # 5 columns # can be changed to be whatever
        # self.result_screen.rows = len(text)
        self.result_screen.rows = 5 # 5 rows
        try:
            for i in range(25): # this range must be rows * cols in order to work correctly
                self.result_screen.add_widget(AsyncImage(source=text[i]))
        except:
            for i in range(len(text)): # this only runs if there are less than rows * cols of the search result
                self.result_screen.add_widget(AsyncImage(source=text[i]))
        print(text) # prints img urls to console


if __name__ == "__main__":
    njh_app = MyApp()
    njh_app.run()
