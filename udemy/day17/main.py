import data
import quiz
class question:
    def __init__(self,t,a):
        self.ques=t
        self.ans=a
l=[]
for i in data.question_data:
    for j in i.keys():
        x=question(j,i[j])
        l.append(x)
q=quiz.quizbrain(l,0)
q.nextquestion(0)