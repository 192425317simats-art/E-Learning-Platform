import reflex as rx
from app.pages.sign_in import sign_in_page
from app.pages.sign_up import sign_up_page
from app.pages.question_pool_page import question_pool_page
from app.pages.take_quiz_page import take_quiz_page
from app.pages.performance_page import performance_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(question_pool_page, route="/")
app.add_page(sign_in_page, route="/sign-in")
app.add_page(sign_up_page, route="/sign-up")
app.add_page(take_quiz_page, route="/take-quiz")
app.add_page(performance_page, route="/performance")