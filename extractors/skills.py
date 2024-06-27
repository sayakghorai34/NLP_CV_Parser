import nltk
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
def load_skills_from_file(file_path):
    with open(file_path, 'r') as file:
        skills = file.readlines()
        skills = [skill.lower() for skill in skills]
    # Strip whitespace and newline characters from each skill
    return [skill.strip() for skill in skills]

# Load skills from external files
technology_skills = load_skills_from_file('extractors/tech_skills.txt')
development_skills = load_skills_from_file('extractors/dev_skills.txt')
business_skills = load_skills_from_file('extractors/business_skills.txt')

# Combine all skills into a single list
SKILLS_DB = technology_skills + development_skills + business_skills

def extract_skills(input_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)
    
    # Remove stop words and non-alphabetic tokens
    filtered_tokens = [w for w in word_tokens if w.lower() not in stop_words and w.isalpha()]
    
    # Generate bigrams and trigrams
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))
    
    found_skills = set()
    
    # Search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)
    
    # Search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)
    
    return found_skills

# Example usage
input_text = "I am proficient in Python, data analysis, machine learning, and business strategy."
skills_found = extract_skills(input_text)
print(skills_found)
