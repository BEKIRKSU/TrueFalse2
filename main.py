from question_model import Question
# Question class from that file imported.
from data import question_data

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(q_text=question_text, q_answer=question_answer)