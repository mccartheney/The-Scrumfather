from textual.app import App, ComposeResult
from textual.widgets import Label, Input, Button


class LoginApp(App):

    CSS = """
    Input.-valid {
        border: tall $success 60%;
    }
    Input.-valid:focus {
        border: tall $success;
    }
    Input {
        margin: 1 1;
    }
    Label {
        margin: 1 2;
    }
    Button {
        margin: 1 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Enter your login credentials.")
        yield Input(placeholder="Username", id="username")
        yield Input(placeholder="Password", password=True, id="password")
        yield Button("Login", id="login_button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "login_button":
            username = self.query_one("#username", Input).value
            password = self.query_one("#password", Input).value
            self.handle_login(username, password)

    def handle_login(self, username: str, password: str) -> None:
        if username and password:
            # Simulate API call
            self.query_one(Label).update(f"Logged in as {username}.")
        else:
            self.query_one(Label).update("Please enter both username and password.")


app = LoginApp()

if __name__ == "__main__":
    app.run()
