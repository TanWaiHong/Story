import spacy
en = 'en_core_web_sm'
nlp = spacy.load(en)
doc = nlp(u'This is the things that may help you in school')

for token in doc:
    print(token.text, token.pos_)
