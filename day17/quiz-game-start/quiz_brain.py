# TODO: Asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we are at the end of the quiz

'''

# Attributes
question_number = 0
question_list

# Methods
next_question()
'''

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        '''

        :return: A boolean value indicating weather there are questions remaining in the question bank.
        '''
        return len(self.question_list) > self.question_number # the number of question_number is increasing.

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number = self.question_number + 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score = self.score + 1
            print("\nYou got it right!!")

        else:
            print("That's wrong!!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def end_game(self):
        print(f"{45*'-'}")
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")