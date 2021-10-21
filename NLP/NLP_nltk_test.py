from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer
import spacy

porter_stemmer = PorterStemmer()
snowball_stemmer = SnowballStemmer("english")
print(porter_stemmer.stem("fastest"))
print(snowball_stemmer.stem("fastest"))

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'fastest')
for token in doc:
    print(token.lemma_)
