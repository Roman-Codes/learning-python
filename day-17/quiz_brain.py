class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {current_question.text}? (True/False)")
        if answer == current_question.answer:
            self.score += 1

    def still_has_questions(self):
        if (len(self.question_list) - self.question_number) == 0:
            print(f"Final score is {self.score}")
            return False
        else:
            return True
