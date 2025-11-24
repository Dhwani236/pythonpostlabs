# 1: incrementer 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.count = 0  # Initialize the counter

        # Create the main layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create the label to display the count
        self.count_label = Label(text=str(self.count), font_size=50)
        layout.add_widget(self.count_label)

        # Create buttons for incrementing and decrementing
        button_layout = BoxLayout(spacing=10)

        increment_button = Button(text='Increment', font_size=30)
        increment_button.bind(on_press=self.increment_count)
        button_layout.add_widget(increment_button)

        decrement_button = Button(text='Decrement', font_size=30)
        decrement_button.bind(on_press=self.decrement_count)
        button_layout.add_widget(decrement_button)

        layout.add_widget(button_layout)

        return layout

    def increment_count(self, instance):
        self.count += 1
        self.count_label.text = str(self.count)

    def decrement_count(self, instance):
        self.count -= 1
        self.count_label.text = str(self.count)

if __name__ == '__main__':
    CounterApp().run()


# 2: Text Input App
class TextInputApp(App):
    def build(self):
        # Create a vertical box layout to arrange widgets
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create a TextInput widget
        self.text_input = TextInput(
            hint_text='Enter your text here',
            multiline=True,  # Set to False for single-line input
            font_size=20,
            size_hint_y=0.7 # Occupy 70% of vertical space
        )
        layout.add_widget(self.text_input)

        # Create a button to process the text
        process_button = Button(
            text='Process Text',
            font_size=20,
            size_hint_y=0.15 # Occupy 15% of vertical space
        )
        process_button.bind(on_press=self.process_text)
        layout.add_widget(process_button)

        # Create a label to display output
        self.output_label = Label(
            text='Output will appear here',
            font_size=18,
            size_hint_y=0.15 # Occupy 15% of vertical space
        )
        layout.add_widget(self.output_label)

        return layout

    def process_text(self, instance):
        # Get the text from the TextInput widget
        entered_text = self.text_input.text
        
        # Perform some simple processing (e.g., capitalize)
        processed_text = entered_text.upper()
        
        # Update the output label
        self.output_label.text = f'Processed: {processed_text}'

if __name__ == '__main__':
    TextInputApp().run()