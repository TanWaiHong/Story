import spacy

nlp = spacy.load("en_core_web_sm")

my_string = u"Google has its headquarters in Mountain View, " \
            u"California having revenue amounted to 109.65 billion us dollars"

doc = nlp(my_string)

for ent in doc.ents:
    print(ent.text, ent.label_)

my_string = u"Mark Zuckerberg born May 14, 1984 in New York is an American " \
            u"technology entrepreneur and philanthrepist best known for " \
            u"co-founding and leading Facebook as its chairman and CEO"

doc = nlp(my_string)

for ent in doc.ents:
    print(ent.text, ent.label_)

my_string = u"I usually wake up at 9:00 AM. 90% of my daytime goes in " \
            u"learning new things."

doc = nlp(my_string)
for ent in doc.ents:
    print(ent.text, ent.label_)

my_string1 = u"Imagine Dragons are the best band."
my_string2 = u"Imagine dragons come and take over the city."
doc1 = nlp(my_string1)
doc2 = nlp(my_string2)

for ent in doc1.ents:
    print(ent.text, ent.label_)

for ent in doc2.ents:
    print(ent.text, ent.label_)
