import spacy

# Load trained model
nlp = spacy.load("ai/model/model-last")

text = "TAB PARACETAMOL 500 1 Morning 5 Days"

doc = nlp(text)

print("Text:", text)
print("\nEntities:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")
