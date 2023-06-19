from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

new_q = Question("3+3=6", True)

question_bank = []

for question in question_data:
    new_question = Question(question['text'], question['answer'])

    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")