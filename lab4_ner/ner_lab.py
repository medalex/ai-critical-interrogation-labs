from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)

text = """
Apple CEO Tim Cook met with EU officials in Brussels to discuss new regulations.
"""

results = ner(text)

for r in results:
    print(r["word"], r["entity_group"])
