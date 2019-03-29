import nltk
import string as s
import re

input=open("train2017.tsv",'r')
output=open("out.tsv",'w')
text=input.read()
text=text.lower();

text=re.sub(r'http\S+', '', text)
text=re.sub('@[a-zA-Z0-9]+','USER ',text)
text=text.translate(None,s.punctuation)

tokens=nltk.word_tokenize(text)

output.write(text)
input.close()
output.close()
