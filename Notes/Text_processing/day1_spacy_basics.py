import spacy


# Spacy is a NLP library used in processing of text.
# nlp variables here is referencing to the spacy code. so that we can use it.
nlp = spacy.load("en_core_web_sm")
text = """I am a Computer Science student interested in Artificial Intelligence.During my undergraduate studies, I developed a machine learning project.
want to pursue advanced research in AI.
My dream is to start a business and work freely. I want to live in South korea and travel around the world. 
I want to pursue my Master's at Oxford Univeristy.
"""
# doc is variable storing processed text. And we are passing text to nlp which will pass the text from spacy pipleine for the processing.
doc = nlp(text)
# For tokens
print("\nTokens:")
for token in doc:
    print(token.text, token.is_alpha)

# Just for readability
print("===============================================")
# For sentences
print("\nSentences:")
for sentence in doc.sents:
    print(sentence.text)
    print("Number of tokens:" ,len(sentence))

# Just for readability
print("===============================================")
# list stores the sentences of doc
sentences = list(doc.sents)
# To count number of sentences
print("Number of total sentences:",len(sentences))

# Just for readability
print("===============================================")

# For printing whole doc
print("DOCUMENT:")
print(doc.text)

# Just for readability
print("===============================================")

# For printing first token only
print("\nFIRST TOKEN:")
print(doc[0].text)

# Just for readability
print("===============================================")

# For printing first sentence
# This will print a span of doc, span means a part of document.
print("\nFIRST SENTENCE:")
print(list(doc.sents)[0].text)


# Flow:
#                                                                         ->spans
# spacy -> NLP Pipeline -> nlp(text) -> doc(it stores the processed data) ->tokens
#                                                                         ->sentences