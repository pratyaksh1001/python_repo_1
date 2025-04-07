import spacy
model=spacy.load('en_core_web_lg')
s1=model("i am eating a banana")
for i in s1.ents:
    print(i,i.label_)