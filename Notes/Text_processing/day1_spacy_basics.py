import spacy


# Spacy is a NLP library used in processing of text.
# nlp variables here is referencing to the spacy code. so that we can use it.
nlp = spacy.load("en_core_web_sm")
text = """
I am a Computer Science student interested in Artificial Intelligence.
During my undergraduate studies, I developed a machine learning project.
I want to pursue advanced research in AI.
My dream is to start a business and work freely. I want to live in South korea and travel around the world. 
I want to pursue my Master's at Oxford Univeristy.
"""
# doc is variable storing processed text. And we are passing text to nlp which will pass the text from spacy pipleine for the processing.
doc = nlp(text)
print("\nTokens:")
for token in doc:
    print(token.text, token.is_alpha)
