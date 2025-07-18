ethilia/ethilia/main.py

import toga from toga.style import Pack from toga.style.pack import COLUMN, ROW

class EthiliaApp(toga.App): def startup(self): # Root layout main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

# User input field
    self.input = toga.TextInput(placeholder="Type a message...", style=Pack(flex=1))

    # Submit button
    send_button = toga.Button("Send", on_press=self.send_message, style=Pack(padding_top=5))

    # Response display
    self.response_label = toga.Label("Welcome to Ethilia!", style=Pack(padding_top=10))

    # Add widgets to main_box
    main_box.add(self.input)
    main_box.add(send_button)
    main_box.add(self.response_label)

    # Setup main window
    self.main_window = toga.MainWindow(title=self.formal_name)
    self.main_window.content = main_box
    self.main_window.show()

def send_message(self, widget):
    user_input = self.input.value.strip()
    if user_input:
        # Dummy AI response for now
        reply = f"You said: {user_input}"
        self.response_label.text = reply
    self.input.value = ""

def main(): return EthiliaApp("Ethilia", "com.ethilia")

if name == 'main': main().main_loop()

