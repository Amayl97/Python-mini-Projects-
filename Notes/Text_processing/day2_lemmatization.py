import spacy

nlp = spacy.load("en_core_web_sm")

text = """I wanted to study abroad after my high school but I couldn't. So I am going after my graduation. I am studying right now."""

doc = nlp(text)
#Lemmatization does not only convert verbs to their first form. It converts words to their base/dictionary form, called the lemma.
for token in doc:
    print(token.text, "->", token.lemma_)

#Store them in a list
filtered = [
    token.lemma_
    for token in doc
    if not token.is_stop and not token.is_punct
]

print(filtered)