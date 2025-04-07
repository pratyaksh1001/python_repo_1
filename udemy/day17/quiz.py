class quizbrain:
    def __init__(self,ql,qn):
        self.qlist=ql
        self.qnum=0
    def nextquestion(self,score):
        x=input(f"Q.{self.qnum+1} - {self.qlist[self.qnum].ques} choose(True/False): ")
        if x==self.qlist[self.qnum].ans:
            print(f"Correct, your score is: {score}")
            score+=1
        else:
            print(f"Incorrect, your score is: {score}")
        self.qnum+=1