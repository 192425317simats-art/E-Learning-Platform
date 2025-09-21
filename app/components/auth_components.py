import reflex as rx
from app.states.auth_state import AuthState


def auth_form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="text-sm font-medium text-gray-700"),
        rx.el.input(
            placeholder=placeholder,
            type=type,
            name=name,
            required=True,
            class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
        ),
        class_name="w-full",
    )


def sign_in_card() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Welcome Back!",
            class_name="text-center text-3xl font-bold tracking-tight text-gray-900",
        ),
        rx.el.p(
            "Sign in to continue your learning journey.",
            class_name="mt-2 text-center text-sm text-gray-600",
        ),
        rx.el.form(
            rx.el.div(
                auth_form_field("Email address", "you@example.com", "email", "email"),
                auth_form_field("Password", "••••••••", "password", "password"),
                class_name="space-y-6",
            ),
            rx.el.div(
                rx.el.button(
                    "Sign In",
                    type="submit",
                    class_name="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all",
                ),
                class_name="pt-4",
            ),
            rx.el.div(
                rx.el.p("Don't have an account?", class_name="text-sm text-gray-600"),
                rx.el.a(
                    "Sign Up",
                    href="/sign-up",
                    class_name="font-medium text-indigo-600 hover:text-indigo-500",
                ),
                class_name="mt-6 flex justify-center items-center gap-2",
            ),
            on_submit=AuthState.sign_in,
            class_name="mt-8 space-y-6",
        ),
        class_name="w-full max-w-md p-8 space-y-8 bg-white rounded-2xl shadow-lg border border-gray-200",
    )


def sign_up_card() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Create an Account",
            class_name="text-center text-3xl font-bold tracking-tight text-gray-900",
        ),
        rx.el.p(
            "Start your personalized learning path today.",
            class_name="mt-2 text-center text-sm text-gray-600",
        ),
        rx.el.form(
            rx.el.div(
                auth_form_field("Full Name", "Your Name", "text", "name"),
                auth_form_field("Email address", "you@example.com", "email", "email"),
                auth_form_field("Password", "••••••••", "password", "password"),
                class_name="space-y-6",
            ),
            rx.el.div(
                rx.el.button(
                    "Sign Up",
                    type="submit",
                    class_name="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all",
                ),
                class_name="pt-4",
            ),
            rx.el.div(
                rx.el.p("Already have an account?", class_name="text-sm text-gray-600"),
                rx.el.a(
                    "Sign In",
                    href="/sign-in",
                    class_name="font-medium text-indigo-600 hover:text-indigo-500",
                ),
                class_name="mt-6 flex justify-center items-center gap-2",
            ),
            on_submit=AuthState.sign_up,
            class_name="mt-8 space-y-6",
        ),
        class_name="w-full max-w-md p-8 space-y-8 bg-white rounded-2xl shadow-lg border border-gray-200",
    )