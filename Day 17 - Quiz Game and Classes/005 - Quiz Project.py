from data import question_data
from question_model import Question
from quiz_brain import Brain

questions = []

for i in question_data:
    questions.append(Question(i['question'], i['correct_answer']))

brain = Brain(questions)

while brain.has_questions():
    brain.next_question()
print("You have completed the quiz!")
print(f"Your final score was {brain.score}/{brain.questionnumber}")