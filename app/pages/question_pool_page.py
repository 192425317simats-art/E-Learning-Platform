import reflex as rx
from app.states.auth_state import AuthState
from app.states.quiz_state import QuizState
from app.components.dashboard_components import sidebar, header
from app.components.question_pool_components import question_table, question_form_modal


def question_pool_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            rx.el.header(
                rx.el.h1(
                    "Question Pool", class_name="text-2xl font-bold text-gray-800"
                ),
                rx.el.button(
                    rx.icon("plus", class_name="h-4 w-4"),
                    "Add New Question",
                    on_click=lambda: QuizState.open_question_form(None),
                    class_name="ml-auto flex items-center gap-2 py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all",
                ),
                class_name="flex items-center h-16 px-6 border-b border-gray-200 bg-white",
            ),
            rx.el.main(
                rx.el.div(question_table(), class_name="p-6"),
                question_form_modal(),
                class_name="flex-1 overflow-y-auto bg-gray-50",
            ),
            class_name="flex flex-col flex-1",
        ),
        class_name="grid grid-cols-[280px_1fr] h-screen w-full font-['Inter']",
        on_mount=AuthState.check_session,
    )