import spacy

nlp = spacy.load("ai/med_ner_model")

def ai_extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

