"""Simple script for testing the custom Finnish spaCy model."""

import json
from pathlib import Path

import spacy
import pytest

BASE_DIR = Path(__file__).resolve().parent.parent
META_PATH = BASE_DIR / "custom_spacy_model" / "meta.json"

with META_PATH.open() as f:
    version = json.load(f)["version"]

model_path = BASE_DIR / "custom_spacy_model" / f"fi_datahel_spacy-{version}"

if not model_path.exists():
    pytest.skip(f"spaCy model directory {model_path} not found", allow_module_level=True)

nlp = spacy.load(str(model_path))

text_fi = "Jaakko söi puuroa aurinkoisena päivänä Helsingissä vartiokylän puistossa, osoitteessa ylerminkuja 6. " \
           "Jaakko Parantainen käy mielelllään kalassa Helsingin itäpuolella (kaukana) yhdeksän kilometrin päässä sijaitsevassa kallion kaupunginosassa, " \
           "vaikka asuukin mannerheimintien varrella. Osoitteessa Liisankatu 12 U 2. Malmin kalatorilta ostetut Silakat ovat Jaakon herkkua."

doc = nlp(text_fi)
for token in doc:
    print(token.text, token.pos_, token.dep_, token.lemma_, token.ent_type_)

print([(ent.text, ent.label_, ent.ent_id_) for ent in doc.ents])

