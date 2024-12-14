# بسم الله الرحمن الرحيم
# la ilaha illa Allah Mohammed Rassoul Allah
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.core.window import Window

def textFormat(raw_text):
    return arabic_reshaper.reshape(raw_text)  # Reshape the Arabic text

def dikrDict(raw_text, count):
    return {'text': textFormat(raw_text), 'count': count}

dikr = [
    dikrDict("سبحان الله وبحمده", 100),
    dikrDict("أستغفر الله وأتوب إليه", 100),
    dikrDict("لا إلاه إلا الله وحده لا شريك له له الملك وله الحمد وهو على كل شيء قدير", 100),
]

class DikrApp(App):
    def build(self):
        self.count = 0

        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Arabic text reshaping for correct RTL rendering
        self.dikr_index = 0
        self.dikr = dikr[self.dikr_index]

        # Add the reshaped Arabic text to the label
        self.dikr_label = Label(
            text=self.dikr['text'],
            font_size='40sp',
            font_direction='rtl',
            halign='center',
            valign='middle',
            font_name='KacstPoster.ttf'  # Use an Arabic-compatible font
        )
        self.dikr_label.bind(size=self.dikr_label.setter('text_size'))  # Allow text wrapping
        layout.add_widget(self.dikr_label)

        # Add the counter label
        self.counter_label = Label(
            text=f"Count: {self.count}",
            font_size='30sp',
            halign='center'
        )
        layout.add_widget(self.counter_label)

        # Add the increment button
        self.increment_button = Button(
            text="Increment",
            font_size='20sp',
            size_hint=(1, 0.2)
        )
        self.increment_button.bind(on_press=self.increment_count)
        layout.add_widget(self.increment_button)

        # Bind keyboard events to functions
        Window.bind(on_key_down=self.on_key_down)

        return layout

    def on_key_down(self, window, key, scancode, codepoint, modifier):
        if key == 13 or key == 32:  # Enter or Space key
            self.increment_count('')

    def increment_count(self, instance):
        if self.dikr_index > len(dikr) and self.count >= self.dikr['count']:
            return

        self.count += 1

        if self.count > self.dikr['count']:
            if self.dikr_index >= len(dikr) - 1:
                return

            self.count = 0
            self.dikr_index += 1
            self.dik = dikr[self.dikr_index]
            self.counter_label.text = f"Count: {self.count}"
            self.dikr_label.text = dikr[self.dikr_index]['text']

        self.counter_label.text = f"Count: {self.count}"

# Run the app
if __name__ == '__main__':
    DikrApp().run()

