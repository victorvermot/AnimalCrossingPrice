from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.list import MDList, TwoLineListItem, OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton




import sys
sys.path.insert(0, r'database')
from fish import Fish

class MenuScreen(Screen):
    hint_text  = 'Enter a fish name'
    def add_fish(self):
        new_entry = self.ids.check_price.text
        for i in Fish.get_fishes():
            if new_entry == i[0]:
                self.ids.fish_price_text.text = f'{i[0]} vaut {i[1]}'


class AddFishScreen(Screen):
    def add_fish_price(self):
        """Get input and add it to the database"""

        self.my_dialog = MDDialog(title='Confirmation', text=f'Le poisson "{self.ids.get_name.text}" a bien été ajouté.',
                            size_hint=[.5, .5],
                            buttons=[
                                MDRaisedButton(
                                    text="Confirmer", on_release=self.close_dialog
                                ),
                            ])
        self.my_dialog.open()

    def close_dialog(self, obj):
        """Closes the pop up if the user click 'Annuler'"""
        self.my_dialog.dismiss()
        # Erase the input entered by the user

        # Add the input to the database
        new_entry = Fish(self.ids.get_name.text, self.ids.get_price.text)
        new_entry.add_fish()

        self.ids.get_name.text = ''
        self.ids.get_price.text = ''

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()
    secondary_text = StringProperty()

class FishListScreen(Screen):
    def on_pre_enter(self):
        self.ids.container.clear_widgets()
        for i in Fish.get_fishes():
            self.ids.container.add_widget(
                SwipeToDeleteItem(text=f'{i[1]}', secondary_text =f'{i[2]} Clochettes')
            )

class mainApp(MDApp):
    def build(self):
        #self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'

    def remove_item(self, instance):
        Fish.remove_appart(instance.text)
        self.root.ids.FishList.ids.container.remove_widget(instance)



if __name__ == '__main__':
    mainApp().run()
