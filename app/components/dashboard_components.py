import reflex as rx
from app.states.auth_state import AuthState
from app.states.quiz_state import QuizState


def sidebar() -> rx.Component:
    def sidebar_link(text: str, href: str, icon: str) -> rx.Component:
        return rx.el.a(
            rx.icon(icon, class_name="h-5 w-5"),
            rx.el.span(text),
            href=href,
            class_name=rx.cond(
                AuthState.router.page.path == href.lower(),
                "flex items-center gap-3 rounded-lg px-3 py-2 text-indigo-600 bg-indigo-50 transition-all font-medium",
                "flex items-center gap-3 rounded-lg px-3 py-2 text-gray-700 transition-all hover:text-gray-900 hover:bg-gray-100 font-medium",
            ),
        )

    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("book-open", class_name="h-8 w-8 text-indigo-500"),
                rx.el.h1("Learnify", class_name="text-2xl font-bold text-gray-800"),
                class_name="flex items-center gap-3 px-4",
            ),
            rx.el.nav(
                sidebar_link("Question Pool", "/", "database"),
                sidebar_link("Take a Quiz", "/take-quiz", "file-pen"),
                sidebar_link("Performance", "/performance", "bar-chart-3"),
                class_name="flex flex-col gap-1 mt-8",
            ),
            class_name="flex flex-col gap-2",
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={AuthState.current_user['name']}",
                    class_name="h-10 w-10 rounded-full",
                ),
                rx.el.div(
                    rx.el.p(
                        AuthState.current_user["name"],
                        class_name="text-sm font-semibold",
                    ),
                    rx.el.p(
                        AuthState.current_user["email"],
                        class_name="text-xs text-gray-500",
                    ),
                    class_name="flex flex-col",
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.button(
                rx.icon("log-out", class_name="h-5 w-5"),
                on_click=AuthState.sign_out,
                class_name="p-2 rounded-lg hover:bg-gray-200",
            ),
            class_name="mt-auto flex items-center justify-between p-4 bg-gray-50 rounded-lg",
        ),
        class_name="flex h-full max-h-screen flex-col gap-2 bg-white border-r border-gray-200 p-4",
    )


def header(title: str) -> rx.Component:
    return rx.el.header(
        rx.el.h1(title, class_name="text-2xl font-bold text-gray-800"),
        class_name="flex items-center h-16 px-6 border-b border-gray-200 bg-white",
    )


def quiz_card(domain: str) -> rx.Component:
    icon_map = {
        "Physics": "atom",
        "Maths": "calculator",
        "Chemistry": "flask-conical",
        "Ethics": "scale",
        "General Knowledge": "globe",
        "C Programming": "code",
        "Python": "code-2",
        "Data Structures": "binary",
    }
    color_map = {
        "Physics": "bg-blue-100 text-blue-800",
        "Maths": "bg-green-100 text-green-800",
        "Chemistry": "bg-purple-100 text-purple-800",
        "Ethics": "bg-yellow-100 text-yellow-800",
        "General Knowledge": "bg-red-100 text-red-800",
        "C Programming": "bg-gray-100 text-gray-800",
        "Python": "bg-teal-100 text-teal-800",
        "Data Structures": "bg-orange-100 text-orange-800",
    }

    def difficulty_button(text: str, level: str, domain: str) -> rx.Component:
        return rx.el.button(
            text,
            on_click=lambda: QuizState.start_quiz(domain, level),
            class_name="flex-1 py-2 px-2 border border-transparent rounded-md shadow-sm text-xs font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all",
        )

    return rx.el.div(
        rx.el.div(
            rx.icon(icon_map.get(domain, "book"), class_name="h-8 w-8"),
            class_name=f"p-3 rounded-lg w-fit {color_map.get(domain, 'bg-gray-100')}",
        ),
        rx.el.h3(domain, class_name="mt-4 text-lg font-semibold text-gray-800"),
        rx.el.p(
            "Select a difficulty to start.", class_name="mt-1 text-sm text-gray-500"
        ),
        rx.el.div(
            difficulty_button("Easy", "Easy", domain),
            difficulty_button("Medium", "Medium", domain),
            difficulty_button("Hard", "Hard", domain),
            difficulty_button("Mixed", "Mixed", domain),
            class_name="mt-4 flex gap-2",
        ),
        class_name="flex flex-col p-6 bg-white rounded-xl shadow-sm border border-gray-200 hover:shadow-md transition-shadow",
    )


def quiz_interface() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    f"Question {QuizState.current_question_index + 1}/{QuizState.current_quiz_questions.length()}",
                    class_name="text-sm font-medium text-indigo-600",
                ),
                rx.el.h2(
                    QuizState.current_question["text"],
                    class_name="mt-2 text-2xl font-bold text-gray-900",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                rx.foreach(
                    QuizState.current_question["options"],
                    lambda option: rx.el.button(
                        option,
                        on_click=lambda: QuizState.select_answer(
                            QuizState.current_question["id"], option
                        ),
                        class_name=rx.cond(
                            QuizState.selected_answers[QuizState.current_question["id"]]
                            == option,
                            "w-full text-left p-4 rounded-lg border-2 border-indigo-500 bg-indigo-50 transition-all",
                            "w-full text-left p-4 rounded-lg border border-gray-300 hover:bg-gray-50 transition-all",
                        ),
                    ),
                ),
                class_name="space-y-4",
            ),
            rx.el.button(
                "Next",
                on_click=QuizState.next_question,
                class_name="mt-8 w-full py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all",
            ),
            class_name="w-full max-w-3xl p-8 bg-white rounded-2xl shadow-lg border border-gray-200",
        ),
        class_name="flex items-start justify-center p-4 sm:p-6 md:p-8",
    )


def results_modal() -> rx.Component:
    def review_question_card(question: rx.Var, index: rx.Var) -> rx.Component:
        user_answer = QuizState.selected_answers.get(question["id"], "Not Answered")
        is_correct = user_answer == question["correct_answer"]

        def get_option_style(option: rx.Var) -> rx.Var:
            is_user_choice = user_answer == option
            is_correct_choice = question["correct_answer"] == option
            return rx.cond(
                is_correct_choice,
                "p-3 rounded-lg bg-green-100 border border-green-300 text-green-800",
                rx.cond(
                    is_user_choice,
                    "p-3 rounded-lg bg-red-100 border border-red-300 text-red-800",
                    "p-3 rounded-lg bg-gray-100 border border-gray-200",
                ),
            )

        return rx.el.div(
            rx.el.p(
                f"Question {index + 1}: {question['text']}",
                class_name="font-semibold text-gray-800",
            ),
            rx.el.div(
                rx.foreach(
                    question["options"],
                    lambda opt: rx.el.div(opt, class_name=get_option_style(opt)),
                ),
                class_name="mt-3 space-y-2",
            ),
            class_name="p-4 bg-white rounded-lg border border-gray-200",
        )

    return rx.cond(
        QuizState.show_results,
        rx.el.dialog(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Quiz Complete!", class_name="text-2xl font-bold text-gray-900"
                    ),
                    rx.el.p(
                        f"Domain: {QuizState.quiz_result['domain']}",
                        class_name="mt-2 text-gray-600",
                    ),
                    rx.el.div(
                        rx.el.p("Score:", class_name="font-semibold"),
                        rx.el.p(
                            f"{QuizState.quiz_result['score']}%",
                            class_name=rx.cond(
                                QuizState.quiz_result["score"] >= 80,
                                "text-green-600 font-bold",
                                rx.cond(
                                    QuizState.quiz_result["score"] >= 50,
                                    "text-yellow-600 font-bold",
                                    "text-red-600 font-bold",
                                ),
                            ),
                        ),
                        class_name="flex justify-between items-center mt-6 text-lg",
                    ),
                    rx.el.div(
                        rx.el.p("Correct Answers:", class_name="font-semibold"),
                        rx.el.p(
                            f"{QuizState.quiz_result['correct']} / {QuizState.quiz_result['total']}"
                        ),
                        class_name="flex justify-between items-center mt-2 text-md",
                    ),
                    rx.el.div(
                        rx.el.p("Feedback:", class_name="font-semibold mt-6"),
                        rx.el.p(
                            f'''"{QuizState.quiz_result['feedback']}"''',
                            class_name="mt-1 text-gray-700 italic",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h4(
                            "Review Answers",
                            class_name="text-xl font-bold text-gray-800 mt-8 mb-4",
                        ),
                        rx.el.div(
                            rx.foreach(
                                QuizState.current_quiz_questions, review_question_card
                            ),
                            class_name="space-y-4 max-h-[40vh] overflow-y-auto p-2 bg-gray-50 rounded-lg",
                        ),
                    ),
                    rx.el.button(
                        "Close",
                        on_click=QuizState.close_results,
                        class_name="mt-8 w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-all",
                    ),
                    class_name="w-full max-w-4xl p-6 bg-white rounded-2xl shadow-xl border border-gray-200",
                ),
                class_name="fixed inset-0 flex items-center justify-center p-4",
            ),
            class_name="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity z-50",
            open=QuizState.show_results,
        ),
        rx.el.div(),
    )