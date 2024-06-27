# import spacy

# nlp = spacy.load("en_core_web_sm")
# def extract_names(text):
#     text = text.replace('\n',' ')
#     text = text.replace('\t',' ')
#     doc = nlp(text)
#     print(doc)
#     person_names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
#     return person_names

import spacy

nlp = spacy.load("en_core_web_sm")

def extract_names(text):
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    doc = nlp(text)
    
    # Print the identified entities and their labels
    for ent in doc.ents:
        print(ent.text, ent.label_)
    
    # Extract names identified as "PERSON" entities
    person_names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    
    return person_names