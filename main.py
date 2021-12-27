from question_model import Question
from data import question_data,logo
from quiz_brain import QuizBrain

print(logo)
print("\n")

question_bank = []

for question in question_data:
    
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
