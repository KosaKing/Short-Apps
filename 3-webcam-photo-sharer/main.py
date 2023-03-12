from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        query = self.manager.current_screen.ids.user_query.text
        # get wiki picture 
        page = wikipedia.page(query)
        img_link = page.images[0]
        return img_link
    
    def download_image(self):
        # download the image
        HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
        req = requests.get(self.get_image_link(), headers=HEADERS)
        img_path = 'files/image.jpg'
        with open(img_path, 'wb') as file:
            file.write(req.content)
        return img_path
        
    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    
    def build(self):
        return RootWidget()

MainApp().run()