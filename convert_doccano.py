import json
import spacy
from spacy.tokens import DocBin


def normalize_entity(ent):
    """
    Supports all Doccano entity formats
    Returns: start, end, label
    """

    # Case 1: dict format
    if isinstance(ent, dict):
        return ent["start_offset"], ent["end_offset"], ent["label"]

    # Case 2: list format (may contain extra fields)
    if isinstance(ent, list) or isinstance(ent, tuple):
        return ent[0], ent[1], ent[2]

    raise ValueError(f"Unknown entity format: {ent}")


def convert(input_jsonl, output_spacy):
    nlp = spacy.blank("en")
    db = DocBin()

    with open(input_jsonl, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            record = json.loads(line)
            text = record["text"]
            doc = nlp.make_doc(text)

            entities = []

            for ent in record.get("entities", []):
                start, end, label = normalize_entity(ent)

                # ---- FIX WHITESPACE SPANS ----
                while start < end and text[start].isspace():
                    start += 1
                while end > start and text[end - 1].isspace():
                    end -= 1

                if start >= end:
                    continue

                span = doc.char_span(
                    start,
                    end,
                    label=label,
                    alignment_mode="contract"
                )

                if span is not None:
                    entities.append(span)

            doc.ents = entities
            db.add(doc)

    db.to_disk(output_spacy)
    print(f"✔ Converted {input_jsonl} → {output_spacy}")


if __name__ == "__main__":
    convert(
        "data/prescription_ner.jsonl",
        "train.spacy"
    )
