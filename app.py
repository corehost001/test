from flask import Flask
from web_terminal import Terminal

app = Flask(__name__)
app.secret_key = "123"
terminal = Terminal(app, shell_command="/bin/bash")

if __name__ == "__main__":
    app.run(debug=True)
