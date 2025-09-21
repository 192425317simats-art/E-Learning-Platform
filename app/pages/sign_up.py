import reflex as rx
from app.components.auth_components import sign_up_card


def sign_up_page() -> rx.Component:
    return rx.el.div(
        sign_up_card(),
        class_name="min-h-screen flex items-center justify-center bg-gray-50 p-4",
    )