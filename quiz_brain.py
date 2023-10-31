class QuizBrain:
    def __init__(self, bank):
        self.qno=0
        self.qlist=bank
        self.score=0

    def nextq(self):
        choice=input(f"Q{self.qno+1}. {self.qlist[self.qno].text} (True or False)? ")
        self.check(choice)
        self.qno+=1

    def still_has_q(self):
        l=len(self.qlist)
        return self.qno<l

    def check(self, answer1):
        if answer1.lower()==self.qlist[self.qno].ans.lower():
            print("You got it right!")
            self.score+=1
        else:
            print(f"That's wrong. \n The correct answer is {self.qlist[self.qno].ans.lower()}")
        print(f"Your current score is {self.score}/{self.qno+1}.\n")