class Brain:
    def __init__(self, question_list):
        self.questionnumber = 0
        self.score = 0
        self.question_list = question_list

    def has_questions(self):
        return self.questionnumber < len(self.question_list)
    def next_question(self):
        q = self.question_list[self.questionnumber].question
        a = self.question_list[self.questionnumber].answer
        print(f"Your current score is {self.score}/{self.questionnumber}")
        answer = input(f"Q.{self.questionnumber+1}: {q} (True or False): ")
        self.questionnumber += 1
        self.check_answer(a, answer)

    def check_answer(self, correctanswer, answer):
        if correctanswer.lower() == answer.lower():
            print("You got it right!!")
            self.score += 1
        else:
            print("That's wrong :(")
        print(f"The correct answer is {correctanswer}")