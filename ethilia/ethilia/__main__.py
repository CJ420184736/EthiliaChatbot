ethilia/ethilia/main.py

import toga from toga.style import Pack from toga.style.pack import COLUMN, ROW

class EthiliaApp(toga.App): def startup(self): main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

self.input = toga.TextInput(placeholder="Type something...", style=Pack(flex=1))
    send_button = toga.Button("Send", on_press=self.send_message, style=Pack(padding_top=5))
    self.response_label = toga.Label("Welcome to Ethilia!", style=Pack(padding_top=10))

    main_box.add(self.input)
    main_box.add(send_button)
    main_box.add(self.response_label)

    self.main_window = toga.MainWindow(title=self.formal_name)
    self.main_window.content = main_box
    self.main_window.show()

def send_message(self, widget):
    user_input = self.input.value.strip()
    if user_input:
        self.response_label.text = f"🤖 You said: {user_input}"
    self.input.value = ""

def main(): return EthiliaApp("Ethilia", "com.ethilia")

if name == 'main': main().main_loop()

