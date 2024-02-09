import spacy

# Load a SpaCy model
nlp = spacy.load("en_core_web_sm")

# Sample document text
text = "This release impacts the payment gateway API and introduces two new features."

# Process the document
doc = nlp(text)

# Extract entities
entities = [(ent.text, ent.label_) for ent in doc.ents]

# Tokenize and remove stopwords
tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

print("Entities:", entities)
print("Tokens:", tokens)
