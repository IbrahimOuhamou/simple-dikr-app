# بسم الله الرحمن الرحيم
# la ilaha illa Allah Mohammed Rassoul Allah
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.core.window import Window

class DikrApp(App):
    def build(self):
        self.count = 0

        # Create the main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        # Arabic text reshaping for correct RTL rendering
        arabic_text = "سبحان الله وبحمده"
        reshaped_text = arabic_reshaper.reshape(arabic_text)  # Reshape the Arabic text
        bidi_text = get_display(reshaped_text)  # Apply bidirectional algorithm

        # Add the reshaped Arabic text to the label
        self.dikr_label = Label(
            text=bidi_text,
            font_size='40sp',
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
        if self.count < 100:
            self.count += 1
            self.counter_label.text = f"Count: {self.count}"

# Run the app
if __name__ == '__main__':
    DikrApp().run()

