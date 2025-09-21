import reflex as rx
from app.states.auth_state import AuthState
from app.states.quiz_state import QuizState
from app.components.dashboard_components import sidebar, header
from app.components.performance_components import (
    summary_card,
    domain_performance_card,
    performance_chart,
    quiz_history_table,
)


def performance_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.el.div(
            header("Performance Analysis"),
            rx.el.main(
                rx.el.div(
                    summary_card(
                        "Overall Average Score",
                        f"{QuizState.overall_average_score.to_string()}%",
                        "percent",
                    ),
                    summary_card(
                        "Total Quizzes Taken",
                        QuizState.quizzes_taken.to_string(),
                        "list-checks",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Performance by Domain",
                        class_name="text-xl font-semibold text-gray-700 my-6",
                    ),
                    rx.el.div(
                        rx.foreach(
                            QuizState.performance_by_domain.keys(),
                            lambda domain: domain_performance_card(
                                domain, QuizState.performance_by_domain[domain]
                            ),
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6",
                    ),
                ),
                rx.el.div(
                    rx.el.h2(
                        "Quiz Performance Trend",
                        class_name="text-xl font-semibold text-gray-700 my-6",
                    ),
                    rx.cond(
                        QuizState.quiz_history.length() > 0,
                        performance_chart(),
                        rx.el.div(
                            rx.el.p(
                                "No quiz data yet. Take a quiz to see your performance history."
                            ),
                            class_name="text-center py-10 px-6 bg-white rounded-lg shadow-sm border",
                        ),
                    ),
                ),
                rx.el.div(
                    rx.el.h2(
                        "Quiz History",
                        class_name="text-xl font-semibold text-gray-700 my-6",
                    ),
                    rx.cond(
                        QuizState.quiz_history.length() > 0,
                        quiz_history_table(),
                        rx.el.div(
                            rx.el.p("No quiz history to display."),
                            class_name="text-center py-10 px-6 bg-white rounded-lg shadow-sm border",
                        ),
                    ),
                ),
                class_name="p-6 space-y-6",
            ),
            class_name="flex flex-col flex-1 overflow-y-auto bg-gray-50",
        ),
        class_name="grid grid-cols-[280px_1fr] h-screen w-full font-['Inter']",
        on_mount=AuthState.check_session,
    )