import nltk
import string as s
import re

input=open("train2017.tsv",'r')
output=open("out.tsv",'w')
text=input.read()
text=text.lower();

text=re.sub(r'http\S+', '', text)
text=re.sub('@[a-zA-Z0-9_]+','USER',text)
text=text.translate(None,s.punctuation)
dict={}
start=0
end=0
tempstr=''
i=10
while(i>0):
    place1=text.find("\t",start,len(text))
    print text[start:place1]
    #place2=text.find("\t",place1,len(text))
    #print text[start:place2]
    start=place1+1
    i-=1

tokens=nltk.word_tokenize(text)

output.write(text)
input.close()
output.close()
