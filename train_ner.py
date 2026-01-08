import spacy
from spacy.training.example import Example

nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

ner.add_label("MEDICINE")
ner.add_label("FREQUENCY")
ner.add_label("TIME")

for epoch in range(20):
    for text, annotations in TRAIN_DATA:
        example = Example.from_dict(nlp.make_doc(text), annotations)
        nlp.update([example])

nlp.to_disk("ai/med_ner_model")
