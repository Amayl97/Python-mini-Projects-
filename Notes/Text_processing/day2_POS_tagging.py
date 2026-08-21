import spacy

nlp = spacy.load("en_core_web_sm")

text = """I wanted to study abroad after my high school but I couldn't. So I am going after my graduation. I am studying right now."""

doc = nlp(text)

# POS stands for Parts of Speech
#This tells us what a word is in a sentence according to english grammar
for token in doc:
    print(token.text, "->", token.pos_)
