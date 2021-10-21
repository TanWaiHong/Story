import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load("en_core_web_sm")
print(STOP_WORDS)
print(nlp.vocab[u'is'].is_stop)
print(nlp.vocab[u'hello'].is_stop)
print(nlp.vocab[u'with'].is_stop)
