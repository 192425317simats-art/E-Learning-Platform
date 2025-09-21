import reflex as rx
from app.states.quiz_state import QuizState


def summary_card(title: str, value: rx.Var, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, class_name="h-6 w-6 text-gray-500"),
            class_name="p-3 bg-gray-100 rounded-lg",
        ),
        rx.el.div(
            rx.el.p(title, class_name="text-sm font-medium text-gray-600"),
            rx.el.p(value, class_name="text-2xl font-semibold text-gray-900"),
        ),
        class_name="flex items-center gap-4 p-6 bg-white rounded-xl shadow-sm border border-gray-200",
    )


def domain_performance_card(domain: str, stats: rx.Var) -> rx.Component:
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
    return rx.el.div(
        rx.el.div(
            rx.icon(icon_map.get(domain, "book"), class_name="h-7 w-7 text-indigo-600"),
            rx.el.h3(domain, class_name="text-lg font-semibold text-gray-800"),
            class_name="flex items-center gap-3",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p("Avg. Score", class_name="text-sm text-gray-500"),
                rx.el.p(
                    f"{stats['average_score']}%",
                    class_name="font-semibold text-gray-900",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.el.p("Quizzes Taken", class_name="text-sm text-gray-500"),
                rx.el.p(
                    stats["quizzes_taken"], class_name="font-semibold text-gray-900"
                ),
                class_name="text-center",
            ),
            class_name="flex justify-around mt-4 pt-4 border-t border-gray-100",
        ),
        class_name="p-6 bg-white rounded-xl shadow-sm border border-gray-200",
    )


def performance_chart() -> rx.Component:
    return rx.recharts.area_chart(
        rx.recharts.cartesian_grid(stroke_dasharray="3 3"),
        rx.recharts.graphing_tooltip(),
        rx.recharts.x_axis(data_key="id", name="Attempt"),
        rx.recharts.y_axis(domain=[0, 100]),
        rx.recharts.legend(),
        rx.recharts.area(
            type="monotone",
            data_key="score",
            stroke="#8884d8",
            fill="#8884d8",
            fill_opacity=0.3,
        ),
        data=QuizState.quiz_history,
        height=400,
        width="100%",
    )


def quiz_history_table() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th("Attempt", class_name="py-3 px-6 text-left"),
                    rx.el.th("Domain", class_name="py-3 px-6 text-left"),
                    rx.el.th("Score", class_name="py-3 px-6 text-left"),
                    rx.el.th("Date", class_name="py-3 px-6 text-left"),
                )
            ),
            rx.el.tbody(
                rx.foreach(
                    QuizState.quiz_history,
                    lambda result: rx.el.tr(
                        rx.el.td(result["id"], class_name="py-4 px-6"),
                        rx.el.td(result["domain"], class_name="py-4 px-6"),
                        rx.el.td(f"{result['score']}%", class_name="py-4 px-6"),
                        rx.el.td(result["timestamp"], class_name="py-4 px-6"),
                        class_name="border-b border-gray-200 hover:bg-gray-50",
                    ),
                )
            ),
            class_name="w-full text-sm text-left text-gray-500",
        ),
        class_name="overflow-x-auto bg-white rounded-lg shadow border",
    )