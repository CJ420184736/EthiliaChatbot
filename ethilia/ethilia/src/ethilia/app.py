import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from ethilia.chatbot import ask_ethilia


class EthiliaApp(toga.App):
    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN))

        self.input = toga.TextInput(placeholder='Say something...', style=Pack(flex=1))
        self.send_button = toga.Button('Send', on_press=self.send_message, style=Pack(padding=5))
        self.response_box = toga.MultilineTextInput(readonly=True, style=Pack(flex=1, height=400))

        input_row = toga.Box(style=Pack(direction=ROW, padding=5))
        input_row.add(self.input)
        input_row.add(self.send_button)

        self.main_box.add(self.response_box)
        self.main_box.add(input_row)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def send_message(self, widget):
        user_input = self.input.value.strip()
        if user_input:
            self.response_box.value += f"You: {user_input}\n"
            response = ask_ethilia(user_input)
            self.response_box.value += f"Ethilia: {response}\n\n"
            self.input.value = ''


def main():
    return EthiliaApp('Ethilia', 'com.ethilia.app')
