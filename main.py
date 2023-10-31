from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for set in question_data:
    q=set["question"]
    a=set["correct_answer"]
    q1=Question(q, a)
    question_bank.append(q1)

quiz=QuizBrain(question_bank)
while quiz.still_has_q():
    quiz.nextq()

print(f"You have completed the quiz.\nYour final score is {quiz.score}/{quiz.qno}.")