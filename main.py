from question_model import Question
# Question class from that file imported.
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)
    # You can get rid of the "named" parameters and just have them as positional parameters.
    question_bank.append(new_question)

# So we make a new QuizBrain object and when initialising pass ina  list of questions.
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz Completed!!")
print(f"Your total score was: {quiz.score}/{quiz.question_number}")