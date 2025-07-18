ethilia/ethilia/main.py

import toga from toga.style import Pack from toga.style.pack import COLUMN, ROW import requests import os

class EthiliaApp(toga.App): def startup(self): main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

self.input = toga.TextInput(placeholder="Ask something...", style=Pack(flex=1))
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
        self.response_label.text = "🤖 Thinking..."
        try:
            reply = self.ask_groq(user_input)
        except Exception as e:
            reply = f"❌ Error: {e}"
        self.response_label.text = reply
    self.input.value = ""

def ask_groq(self, prompt, max_retries=2):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise Exception("Missing GROQ_API_KEY env var")

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    for attempt in range(max_retries):
        try:
            response = requests.post(url, headers=headers, json=data, timeout=15)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].strip()
        except requests.RequestException as e:
            if attempt == max_retries - 1:
                raise Exception("Groq API error: " + str(e))

def main(): return EthiliaApp("Ethilia", "com.ethilia")

if name == 'main': main().main_loop()

