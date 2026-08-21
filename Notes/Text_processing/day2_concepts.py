import  spacy

nlp = spacy.load("en_core_web_sm")

text = """I want to pursue master's in Computer Engineering but not in Pakistan. I will study at OXFORD! By the way, I have to take a break before that."""

doc = nlp(text)

# token.is_stop tells whether it is a stop word or not.
# Stop words are common words that often carry little useful meaning for a specific text-analysis task. such as I, am, is, a, an etc
for token in doc:
    print(token.text, "->", token.is_stop)

# Create an array of words that are not stop words
#Punctuation is not considered as stop word. So it will be added in array too.
filtered_words = []
for token in doc:
    if not token.is_stop:
        filtered_words.append(token.text)

print(filtered_words)

# To filter stop words and punctuation
filtered_words_punc = []
for token in doc:
    if not token.is_stop and not token.is_punct:
        filtered_words_punc.append(token.text)

print(filtered_words_punc)

# Same task as above just with different syntax
# this is called list comprehension
filtered = [
    token.text
    for token in doc
    if not token.is_stop and not token.is_punct
]

print(filtered)
