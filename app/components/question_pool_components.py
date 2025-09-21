import reflex as rx
from app.states.quiz_state import QuizState, Question


def question_table() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th("Question", class_name="py-3 px-6 text-left"),
                    rx.el.th("Domain", class_name="py-3 px-6 text-left"),
                    rx.el.th("Difficulty", class_name="py-3 px-6 text-left"),
                    rx.el.th("Actions", class_name="py-3 px-6 text-center"),
                )
            ),
            rx.el.tbody(
                rx.foreach(
                    QuizState.question_pool,
                    lambda question: rx.el.tr(
                        rx.el.td(question["text"], class_name="py-4 px-6"),
                        rx.el.td(question["domain"], class_name="py-4 px-6"),
                        rx.el.td(
                            rx.el.span(
                                question["difficulty"],
                                class_name=rx.cond(
                                    question["difficulty"] == "Easy",
                                    "bg-green-100 text-green-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                                    rx.cond(
                                        question["difficulty"] == "Medium",
                                        "bg-yellow-100 text-yellow-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                                        "bg-red-100 text-red-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded-full",
                                    ),
                                ),
                            ),
                            class_name="py-4 px-6",
                        ),
                        rx.el.td(
                            rx.el.button(
                                rx.icon("copy", class_name="h-4 w-4"),
                                on_click=lambda: QuizState.open_question_form(question),
                                class_name="p-2 hover:bg-gray-100 rounded-md",
                            ),
                            rx.el.button(
                                rx.icon("trash-2", class_name="h-4 w-4 text-red-600"),
                                on_click=lambda: QuizState.delete_question(
                                    question["id"]
                                ),
                                class_name="p-2 hover:bg-gray-100 rounded-md",
                            ),
                            class_name="py-4 px-6 text-center",
                        ),
                        class_name="border-b border-gray-200 hover:bg-gray-50",
                    ),
                )
            ),
            class_name="w-full text-sm text-left text-gray-500",
        ),
        class_name="overflow-x-auto bg-white rounded-lg shadow border",
    )


def question_form_modal() -> rx.Component:
    def form_field(
        label: str,
        name: str,
        default_value: rx.Var,
        placeholder: str,
        type: str = "text",
    ) -> rx.Component:
        return rx.el.div(
            rx.el.label(label, class_name="block text-sm font-medium text-gray-700"),
            rx.el.input(
                name=name,
                default_value=default_value,
                placeholder=placeholder,
                type=type,
                required=True,
                class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
            ),
        )

    return rx.cond(
        QuizState.show_question_form,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        rx.cond(
                            QuizState.editing_question,
                            "Edit Question",
                            "Add New Question",
                        ),
                        class_name="text-lg font-medium leading-6 text-gray-900",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="h-5 w-5"),
                        on_click=QuizState.close_question_form,
                        class_name="p-1 rounded-full hover:bg-gray-200",
                    ),
                    class_name="flex items-center justify-between pb-4 border-b",
                ),
                rx.el.form(
                    rx.el.div(
                        form_field(
                            "Question Text",
                            "text",
                            rx.cond(
                                QuizState.editing_question,
                                QuizState.editing_question["text"],
                                "",
                            ),
                            "What is...?",
                        ),
                        form_field(
                            "Options (comma-separated)",
                            "options",
                            rx.cond(
                                QuizState.editing_question,
                                QuizState.editing_question["options"].join(", "),
                                "",
                            ),
                            "Option 1, Option 2, ...",
                        ),
                        form_field(
                            "Correct Answer",
                            "correct_answer",
                            rx.cond(
                                QuizState.editing_question,
                                QuizState.editing_question["correct_answer"],
                                "",
                            ),
                            "The correct option",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Domain",
                                class_name="block text-sm font-medium text-gray-700",
                            ),
                            rx.el.select(
                                rx.foreach(
                                    QuizState.domains,
                                    lambda d: rx.el.option(d, value=d),
                                ),
                                name="domain",
                                default_value=rx.cond(
                                    QuizState.editing_question,
                                    QuizState.editing_question["domain"],
                                    QuizState.domains[0],
                                ),
                                class_name="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Difficulty",
                                class_name="block text-sm font-medium text-gray-700",
                            ),
                            rx.el.select(
                                rx.foreach(
                                    ["Easy", "Medium", "Hard"],
                                    lambda d: rx.el.option(d, value=d),
                                ),
                                name="difficulty",
                                default_value=rx.cond(
                                    QuizState.editing_question,
                                    QuizState.editing_question["difficulty"],
                                    "Easy",
                                ),
                                class_name="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md",
                            ),
                        ),
                        class_name="space-y-4 py-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            on_click=QuizState.close_question_form,
                            type="button",
                            class_name="inline-flex justify-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2",
                        ),
                        rx.el.button(
                            "Save Question",
                            type="submit",
                            class_name="ml-3 inline-flex justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2",
                        ),
                        class_name="flex justify-end pt-4 border-t",
                    ),
                    on_submit=QuizState.save_question,
                ),
                class_name="bg-white p-6 rounded-lg shadow-xl w-full max-w-2xl",
            ),
            class_name="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center p-4 z-50",
        ),
    )