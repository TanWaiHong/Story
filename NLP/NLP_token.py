import spacy

nlp = spacy.load('en_core_web_sm')  # Loads the spacy en model into a python object
doc = nlp(u'Google release "Move Mirror" AI experiment that matches your pose from 80,000 image')
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)

doc = nlp(u'I am learning how to build chatbots')
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)

doc = nlp(u'fastest')
for token in doc:
    print(token.lemma_)