from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    question_category = question["category"]
    new_question = Question(question_text, question_answer, question_category)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score:{quiz.score}/{quiz.question_number}")
