import spacy

# Load trained NER model
nlp = spacy.load("ai/model/model-last")

def extract_entities(text):
    doc = nlp(text)
    entities = []

    for ent in doc.ents:
        entities.append({
            "label": ent.label_,
            "value": ent.text
        })

    return entities
