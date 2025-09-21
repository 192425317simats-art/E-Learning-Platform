import reflex as rx
from app.states.auth_state import AuthState
from app.states.quiz_state import QuizState
from app.components.dashboard_components import sidebar, header, quiz_card
from app.components.dashboard_components import quiz_interface, results_modal


def take_quiz_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header("Take a Quiz"),
            rx.el.main(
                rx.cond(
                    QuizState.is_quiz_active,
                    quiz_interface(),
                    rx.el.div(
                        rx.el.h2(
                            "Choose a Domain",
                            class_name="text-xl font-semibold text-gray-700 mb-6",
                        ),
                        rx.el.div(
                            rx.foreach(QuizState.domains, quiz_card),
                            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
                        ),
                        class_name="p-6",
                    ),
                ),
                results_modal(),
                class_name="flex-1 overflow-y-auto bg-gray-50",
            ),
            class_name="flex flex-col flex-1",
        ),
        class_name="grid grid-cols-[280px_1fr] h-screen w-full font-['Inter']",
        on_mount=AuthState.check_session,
    )