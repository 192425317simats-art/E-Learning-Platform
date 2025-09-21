import reflex as rx
from typing import TypedDict


class User(TypedDict):
    email: str
    name: str
    password: str


class AuthState(rx.State):
    users: dict[str, User] = {
        "student@example.com": {
            "email": "student@example.com",
            "name": "Demo Student",
            "password": "password123",
        }
    }
    current_user: User | None = None

    @rx.var
    def is_authenticated(self) -> bool:
        return self.current_user is not None

    @rx.event
    def sign_up(self, form_data: dict):
        email = form_data["email"].lower()
        if email in self.users:
            yield rx.toast("Email already in use.", duration=3000)
            return
        new_user: User = {
            "email": email,
            "name": form_data["name"],
            "password": form_data["password"],
        }
        self.users[email] = new_user
        self.current_user = new_user
        return rx.redirect("/")

    @rx.event
    def sign_in(self, form_data: dict):
        email = form_data["email"].lower()
        user = self.users.get(email)
        if user and user["password"] == form_data["password"]:
            self.current_user = user
            return rx.redirect("/")
        else:
            yield rx.toast("Invalid email or password.", duration=3000)
            return

    @rx.event
    def sign_out(self):
        self.current_user = None
        return rx.redirect("/sign-in")

    @rx.event
    def check_session(self):
        if not self.is_authenticated:
            return rx.redirect("/sign-in")