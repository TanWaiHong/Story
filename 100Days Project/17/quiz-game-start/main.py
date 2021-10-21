from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list()
for element in question_data:
    element_text = element["text"]
    element_answer = element["answer"]
    new_question = Question(element_text, element_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
