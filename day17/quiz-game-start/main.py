from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for item in question_data:
    question_text = item['question']
    question_answer = item['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
quiz_brain = QuizBrain(question_bank)
# if the quiz still has questions remaining:
while quiz_brain.still_has_question():

    quiz_brain.next_question()

quiz_brain.end_game()