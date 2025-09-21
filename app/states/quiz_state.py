import reflex as rx
import random
from typing import TypedDict, Literal
import datetime


class Question(TypedDict):
    id: int
    text: str
    options: list[str]
    correct_answer: str
    difficulty: Literal["Easy", "Medium", "Hard"]
    domain: str


class QuizResult(TypedDict):
    id: int
    domain: str
    score: float
    correct: int
    total: int
    feedback: str
    timestamp: str


class QuizState(rx.State):
    question_pool: list[Question] = [
        {
            "id": 1,
            "text": "What is the SI unit of force?",
            "options": ["Watt", "Joule", "Newton", "Pascal"],
            "correct_answer": "Newton",
            "difficulty": "Easy",
            "domain": "Physics",
        },
        {
            "id": 27,
            "text": "What is the law of conservation of energy?",
            "options": [
                "Energy can be created",
                "Energy cannot be created or destroyed",
                "Energy is always increasing",
                "Energy is always decreasing",
            ],
            "correct_answer": "Energy cannot be created or destroyed",
            "difficulty": "Easy",
            "domain": "Physics",
        },
        {
            "id": 28,
            "text": "What property of an object is a measure of its inertia?",
            "options": ["Mass", "Weight", "Velocity", "Density"],
            "correct_answer": "Mass",
            "difficulty": "Easy",
            "domain": "Physics",
        },
        {
            "id": 29,
            "text": "Which type of lens is used to correct nearsightedness?",
            "options": ["Concave", "Convex", "Plano-convex", "Bifocal"],
            "correct_answer": "Concave",
            "difficulty": "Easy",
            "domain": "Physics",
        },
        {
            "id": 30,
            "text": "What is the speed of light in a vacuum?",
            "options": [
                "300,000 km/s",
                "150,000 km/s",
                "500,000 km/s",
                "1,000,000 km/s",
            ],
            "correct_answer": "300,000 km/s",
            "difficulty": "Easy",
            "domain": "Physics",
        },
        {
            "id": 2,
            "text": "What is the formula for kinetic energy?",
            "options": ["mgh", "1/2 mv^2", "ma", "F/A"],
            "correct_answer": "1/2 mv^2",
            "difficulty": "Medium",
            "domain": "Physics",
        },
        {
            "id": 31,
            "text": "What is Ohm's Law?",
            "options": ["V=IR", "P=VI", "F=ma", "E=mc^2"],
            "correct_answer": "V=IR",
            "difficulty": "Medium",
            "domain": "Physics",
        },
        {
            "id": 32,
            "text": "What is the principle of a transformer?",
            "options": [
                "Mutual induction",
                "Self-induction",
                "Capacitance",
                "Resistance",
            ],
            "correct_answer": "Mutual induction",
            "difficulty": "Medium",
            "domain": "Physics",
        },
        {
            "id": 33,
            "text": "What is the Doppler effect?",
            "options": [
                "Change in frequency of a wave in relation to an observer",
                "Bending of light",
                "Splitting of light",
                "Reflection of sound",
            ],
            "correct_answer": "Change in frequency of a wave in relation to an observer",
            "difficulty": "Medium",
            "domain": "Physics",
        },
        {
            "id": 34,
            "text": "What are the three modes of heat transfer?",
            "options": [
                "Conduction, Convection, Radiation",
                "Conduction, Induction, Radiation",
                "Convection, Refraction, Diffusion",
                "Radiation, Reflection, Absorption",
            ],
            "correct_answer": "Conduction, Convection, Radiation",
            "difficulty": "Medium",
            "domain": "Physics",
        },
        {
            "id": 3,
            "text": "What does E=mc^2 represent?",
            "options": [
                "Theory of Relativity",
                "Quantum Mechanics",
                "Newton's Second Law",
                "Ohm's Law",
            ],
            "correct_answer": "Theory of Relativity",
            "difficulty": "Hard",
            "domain": "Physics",
        },
        {
            "id": 35,
            "text": "What are Maxwell's Equations?",
            "options": [
                "A set of equations describing electromagnetism",
                "Equations for thermodynamics",
                "Laws of motion",
                "Principles of quantum mechanics",
            ],
            "correct_answer": "A set of equations describing electromagnetism",
            "difficulty": "Hard",
            "domain": "Physics",
        },
        {
            "id": 36,
            "text": "What is quantum entanglement?",
            "options": [
                "A physical phenomenon where particles are linked in such a way that their fates are intertwined",
                "A type of chemical bond",
                "A form of energy",
                "A theory about black holes",
            ],
            "correct_answer": "A physical phenomenon where particles are linked in such a way that their fates are intertwined",
            "difficulty": "Hard",
            "domain": "Physics",
        },
        {
            "id": 37,
            "text": "What is the Heisenberg Uncertainty Principle?",
            "options": [
                "It is impossible to know both the position and momentum of a particle simultaneously",
                "Energy is conserved",
                "For every action, there is an equal and opposite reaction",
                "The universe is expanding",
            ],
            "correct_answer": "It is impossible to know both the position and momentum of a particle simultaneously",
            "difficulty": "Hard",
            "domain": "Physics",
        },
        {
            "id": 38,
            "text": "What is a black hole singularity?",
            "options": [
                "A point of infinite density",
                "The event horizon",
                "A wormhole",
                "A white dwarf",
            ],
            "correct_answer": "A point of infinite density",
            "difficulty": "Hard",
            "domain": "Physics",
        },
        {
            "id": 5,
            "text": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_answer": "4",
            "difficulty": "Easy",
            "domain": "Maths",
        },
        {
            "id": 39,
            "text": "What is 10 * 5?",
            "options": ["45", "50", "55", "60"],
            "correct_answer": "50",
            "difficulty": "Easy",
            "domain": "Maths",
        },
        {
            "id": 40,
            "text": "How many sides does a triangle have?",
            "options": ["2", "3", "4", "5"],
            "correct_answer": "3",
            "difficulty": "Easy",
            "domain": "Maths",
        },
        {
            "id": 41,
            "text": "What is a prime number?",
            "options": [
                "A number divisible only by 1 and itself",
                "An even number",
                "An odd number",
                "A number greater than 100",
            ],
            "correct_answer": "A number divisible only by 1 and itself",
            "difficulty": "Easy",
            "domain": "Maths",
        },
        {
            "id": 42,
            "text": "What is the area of a square with side length 5?",
            "options": ["20", "25", "30", "15"],
            "correct_answer": "25",
            "difficulty": "Easy",
            "domain": "Maths",
        },
        {
            "id": 6,
            "text": "What is the value of Pi (to 2 decimal places)?",
            "options": ["3.12", "3.14", "3.16", "3.18"],
            "correct_answer": "3.14",
            "difficulty": "Medium",
            "domain": "Maths",
        },
        {
            "id": 43,
            "text": "What is the Pythagorean theorem?",
            "options": ["a^2 + b^2 = c^2", "a+b=c", "a*b=c", "a-b=c"],
            "correct_answer": "a^2 + b^2 = c^2",
            "difficulty": "Medium",
            "domain": "Maths",
        },
        {
            "id": 44,
            "text": "Solve for x: 2x + 5 = 15",
            "options": ["3", "5", "7", "10"],
            "correct_answer": "5",
            "difficulty": "Medium",
            "domain": "Maths",
        },
        {
            "id": 45,
            "text": "What is the formula for the area of a circle?",
            "options": ["2πr", "πr^2", "πd", "2πd"],
            "correct_answer": "πr^2",
            "difficulty": "Medium",
            "domain": "Maths",
        },
        {
            "id": 46,
            "text": "What is a factorial of a number?",
            "options": [
                "The product of all positive integers up to that number",
                "The sum of all positive integers up to that number",
                "The number multiplied by itself",
                "The square root of the number",
            ],
            "correct_answer": "The product of all positive integers up to that number",
            "difficulty": "Medium",
            "domain": "Maths",
        },
        {
            "id": 7,
            "text": "What is the integral of 2x dx?",
            "options": ["x^2 + C", "2x^2 + C", "x + C", "2 + C"],
            "correct_answer": "x^2 + C",
            "difficulty": "Hard",
            "domain": "Maths",
        },
        {
            "id": 47,
            "text": "What is a derivative?",
            "options": [
                "The rate of change of a function",
                "The area under a curve",
                "The maximum value of a function",
                "The minimum value of a function",
            ],
            "correct_answer": "The rate of change of a function",
            "difficulty": "Hard",
            "domain": "Maths",
        },
        {
            "id": 48,
            "text": "What are complex numbers?",
            "options": [
                "Numbers with a real and imaginary part",
                "Irrational numbers",
                "Negative numbers",
                "Prime numbers",
            ],
            "correct_answer": "Numbers with a real and imaginary part",
            "difficulty": "Hard",
            "domain": "Maths",
        },
        {
            "id": 49,
            "text": "What is Euler's identity?",
            "options": [
                "e^(iπ) + 1 = 0",
                "e^x",
                "sin^2(x) + cos^2(x) = 1",
                "a^2+b^2=c^2",
            ],
            "correct_answer": "e^(iπ) + 1 = 0",
            "difficulty": "Hard",
            "domain": "Maths",
        },
        {
            "id": 50,
            "text": "What is a Fourier Transform?",
            "options": [
                "A mathematical transform that decomposes a function into its constituent frequencies",
                "A type of matrix",
                "A geometric shape",
                "A statistical method",
            ],
            "correct_answer": "A mathematical transform that decomposes a function into its constituent frequencies",
            "difficulty": "Hard",
            "domain": "Maths",
        },
        {
            "id": 8,
            "text": "What is the chemical symbol for water?",
            "options": ["O2", "H2O", "CO2", "NaCl"],
            "correct_answer": "H2O",
            "difficulty": "Easy",
            "domain": "Chemistry",
        },
        {
            "id": 9,
            "text": "What is the pH of a neutral substance?",
            "options": ["0", "7", "14", "1"],
            "correct_answer": "7",
            "difficulty": "Medium",
            "domain": "Chemistry",
        },
        {
            "id": 10,
            "text": "What is the most abundant gas in Earth's atmosphere?",
            "options": ["Oxygen", "Hydrogen", "Nitrogen", "Carbon Dioxide"],
            "correct_answer": "Nitrogen",
            "difficulty": "Hard",
            "domain": "Chemistry",
        },
        {
            "id": 11,
            "text": "Which ethical theory focuses on consequences?",
            "options": ["Deontology", "Virtue Ethics", "Consequentialism", "Egoism"],
            "correct_answer": "Consequentialism",
            "difficulty": "Easy",
            "domain": "Ethics",
        },
        {
            "id": 12,
            "text": "What is the 'Golden Rule'?",
            "options": [
                "Do unto others as you would have them do unto you",
                "The ends justify the means",
                "Might makes right",
                "Survival of the fittest",
            ],
            "correct_answer": "Do unto others as you would have them do unto you",
            "difficulty": "Medium",
            "domain": "Ethics",
        },
        {
            "id": 13,
            "text": "What is Kant's Categorical Imperative?",
            "options": [
                "Act only according to that maxim whereby you can at the same time will that it should become a universal law",
                "Seek the greatest good for the greatest number",
                "Follow your heart",
                "Power is the ultimate goal",
            ],
            "correct_answer": "Act only according to that maxim whereby you can at the same time will that it should become a universal law",
            "difficulty": "Hard",
            "domain": "Ethics",
        },
        {
            "id": 4,
            "text": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "Mars",
            "difficulty": "Easy",
            "domain": "General Knowledge",
        },
        {
            "id": 14,
            "text": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": "Paris",
            "difficulty": "Easy",
            "domain": "General Knowledge",
        },
        {
            "id": 15,
            "text": "Who wrote 'Hamlet'?",
            "options": [
                "Charles Dickens",
                "William Shakespeare",
                "Jane Austen",
                "Mark Twain",
            ],
            "correct_answer": "William Shakespeare",
            "difficulty": "Medium",
            "domain": "General Knowledge",
        },
        {
            "id": 16,
            "text": "In which year did the Titanic sink?",
            "options": ["1905", "1912", "1918", "1923"],
            "correct_answer": "1912",
            "difficulty": "Hard",
            "domain": "General Knowledge",
        },
        {
            "id": 17,
            "text": "Which keyword is used to define a constant in C?",
            "options": ["const", "let", "var", "define"],
            "correct_answer": "const",
            "difficulty": "Easy",
            "domain": "C Programming",
        },
        {
            "id": 21,
            "text": "How do you declare a pointer in C?",
            "options": ["int* p;", "int p;", "ptr p;", "*int p;"],
            "correct_answer": "int* p;",
            "difficulty": "Easy",
            "domain": "C Programming",
        },
        {
            "id": 22,
            "text": "What is the purpose of the `malloc` function in C?",
            "options": [
                "To allocate memory",
                "To free memory",
                "To reallocate memory",
                "To copy memory",
            ],
            "correct_answer": "To allocate memory",
            "difficulty": "Medium",
            "domain": "C Programming",
        },
        {
            "id": 23,
            "text": "What is a dangling pointer?",
            "options": [
                "A pointer to a deallocated memory block",
                "A null pointer",
                "An uninitialized pointer",
                "A pointer to a pointer",
            ],
            "correct_answer": "A pointer to a deallocated memory block",
            "difficulty": "Hard",
            "domain": "C Programming",
        },
        {
            "id": 20,
            "text": "What is the main purpose of a 'for' loop in Python?",
            "options": [
                "To define a function",
                "To handle exceptions",
                "To iterate over a sequence",
                "To declare a variable",
            ],
            "correct_answer": "To iterate over a sequence",
            "difficulty": "Easy",
            "domain": "Python",
        },
        {
            "id": 24,
            "text": "What is a list comprehension in Python?",
            "options": [
                "A way to create lists",
                "A type of loop",
                "A function for lists",
                "A data type",
            ],
            "correct_answer": "A way to create lists",
            "difficulty": "Medium",
            "domain": "Python",
        },
        {
            "id": 25,
            "text": "What does a decorator do in Python?",
            "options": [
                "Modifies a function or class",
                "Deletes a function",
                "Creates a variable",
                "Styles text",
            ],
            "correct_answer": "Modifies a function or class",
            "difficulty": "Hard",
            "domain": "Python",
        },
        {
            "id": 18,
            "text": "Which data structure uses LIFO?",
            "options": ["Queue", "Stack", "Array", "Linked List"],
            "correct_answer": "Stack",
            "difficulty": "Easy",
            "domain": "Data Structures",
        },
        {
            "id": 19,
            "text": "What is the time complexity of a binary search?",
            "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"],
            "correct_answer": "O(log n)",
            "difficulty": "Medium",
            "domain": "Data Structures",
        },
        {
            "id": 26,
            "text": "What is a hash collision?",
            "options": [
                "Two keys have the same hash value",
                "A key is not found",
                "A hash table is full",
                "A key has a null value",
            ],
            "correct_answer": "Two keys have the same hash value",
            "difficulty": "Hard",
            "domain": "Data Structures",
        },
    ]
    domains: list[str] = [
        "Physics",
        "Maths",
        "Chemistry",
        "Ethics",
        "General Knowledge",
        "C Programming",
        "Python",
        "Data Structures",
    ]
    current_quiz_questions: list[Question] = []
    current_question_index: int = 0
    selected_answers: dict[int, str] = {}
    quiz_result: QuizResult | None = None
    is_quiz_active: bool = False
    show_results: bool = False
    quiz_history: list[QuizResult] = []
    editing_question: Question | None = None
    show_question_form: bool = False

    @rx.event
    def open_question_form(self, question: Question | None = None):
        if question is not None:
            self.editing_question = question
        else:
            self.editing_question = None
        self.show_question_form = True

    @rx.event
    def close_question_form(self):
        self.show_question_form = False
        self.editing_question = None

    @rx.event
    def save_question(self, form_data: dict):
        options = [o.strip() for o in form_data["options"].split(",")]
        if self.editing_question:
            index = next(
                (
                    i
                    for i, q in enumerate(self.question_pool)
                    if q["id"] == self.editing_question["id"]
                ),
                -1,
            )
            if index != -1:
                self.question_pool[index]["text"] = form_data["text"]
                self.question_pool[index]["options"] = options
                self.question_pool[index]["correct_answer"] = form_data[
                    "correct_answer"
                ]
                self.question_pool[index]["difficulty"] = form_data["difficulty"]
                self.question_pool[index]["domain"] = form_data["domain"]
        else:
            new_id = (
                max((q["id"] for q in self.question_pool)) + 1
                if self.question_pool
                else 1
            )
            new_question: Question = {
                "id": new_id,
                "text": form_data["text"],
                "options": options,
                "correct_answer": form_data["correct_answer"],
                "difficulty": form_data["difficulty"],
                "domain": form_data["domain"],
            }
            self.question_pool.append(new_question)
        self.close_question_form()

    @rx.event
    def delete_question(self, question_id: int):
        self.question_pool = [q for q in self.question_pool if q["id"] != question_id]

    @rx.var
    def overall_average_score(self) -> float:
        if not self.quiz_history:
            return 0.0
        total_score = sum((res["score"] for res in self.quiz_history))
        return round(total_score / len(self.quiz_history), 2)

    @rx.var
    def quizzes_taken(self) -> int:
        return len(self.quiz_history)

    @rx.var
    def performance_by_domain(self) -> dict[str, dict[str, float | int]]:
        domain_performance = {}
        for domain in self.domains:
            domain_quizzes = [
                res for res in self.quiz_history if res["domain"] == domain
            ]
            if not domain_quizzes:
                continue
            avg_score = sum((q["score"] for q in domain_quizzes)) / len(domain_quizzes)
            domain_performance[domain] = {
                "average_score": round(avg_score, 2),
                "quizzes_taken": len(domain_quizzes),
            }
        return domain_performance

    @rx.var
    def current_question(self) -> Question | None:
        if self.is_quiz_active and self.current_question_index < len(
            self.current_quiz_questions
        ):
            return self.current_quiz_questions[self.current_question_index]
        return None

    @rx.event
    def start_quiz(self, domain: str, difficulty: str):
        self.is_quiz_active = True
        self.show_results = False
        self.current_question_index = 0
        self.selected_answers = {}
        self.quiz_result = None
        all_domain_questions = [q for q in self.question_pool if q["domain"] == domain]
        quiz_questions = []
        if difficulty == "Mixed":
            easy_questions = [
                q for q in all_domain_questions if q["difficulty"] == "Easy"
            ]
            medium_questions = [
                q for q in all_domain_questions if q["difficulty"] == "Medium"
            ]
            hard_questions = [
                q for q in all_domain_questions if q["difficulty"] == "Hard"
            ]
            if len(easy_questions) >= 2:
                quiz_questions.extend(random.sample(easy_questions, 2))
            else:
                quiz_questions.extend(easy_questions)
            if len(medium_questions) >= 2:
                quiz_questions.extend(random.sample(medium_questions, 2))
            else:
                quiz_questions.extend(medium_questions)
            if len(hard_questions) >= 1:
                quiz_questions.extend(random.sample(hard_questions, 1))
            else:
                quiz_questions.extend(hard_questions)
        else:
            level_questions = [
                q for q in all_domain_questions if q["difficulty"] == difficulty
            ]
            if len(level_questions) >= 5:
                quiz_questions = random.sample(level_questions, 5)
            else:
                quiz_questions = level_questions
        if not quiz_questions:
            yield rx.toast(
                "Not enough questions available for this selection.", duration=3000
            )
            self.is_quiz_active = False
            return
        random.shuffle(quiz_questions)
        self.current_quiz_questions = quiz_questions

    @rx.event
    def select_answer(self, question_id: int, answer: str):
        self.selected_answers[question_id] = answer

    @rx.event
    def next_question(self):
        if self.current_question_index < len(self.current_quiz_questions) - 1:
            self.current_question_index += 1
        else:
            self.submit_quiz()

    @rx.event
    def submit_quiz(self):
        correct_answers = 0
        total_questions = len(self.current_quiz_questions)
        for question in self.current_quiz_questions:
            if self.selected_answers.get(question["id"]) == question["correct_answer"]:
                correct_answers += 1
        score = correct_answers / total_questions * 100 if total_questions > 0 else 0
        feedback = "Excellent work!"
        if score < 50:
            feedback = "You can do better. Keep practicing!"
        elif score < 80:
            feedback = "Good job! A little more practice will make you perfect."
        new_id = len(self.quiz_history) + 1
        self.quiz_result = {
            "id": new_id,
            "domain": self.current_quiz_questions[0]["domain"]
            if self.current_quiz_questions
            else "",
            "score": round(score, 2),
            "correct": correct_answers,
            "total": total_questions,
            "feedback": feedback,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        self.quiz_history.append(self.quiz_result)
        self.is_quiz_active = False
        self.show_results = True

    @rx.event
    def close_results(self):
        self.show_results = False
        self.current_quiz_questions = []
        self.current_question_index = 0
        self.selected_answers = {}
        self.quiz_result = None