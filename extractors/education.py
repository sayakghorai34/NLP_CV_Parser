import nltk
from nltk.stem import WordNetLemmatizer

# Updated list of qualifications
QUALIFICATIONS = [
    'M.S.', 'B.S.', '10th', '12th', '10+2', 'M.A', 'B.A', 'Graduate',
    'Masters', 'Undergraduate', 'UG', 'PG', 'Ph.D.', 'MBA', 'B.Tech',
    'B.E.', 'M.E.', 'M.Tech', 'LLB', 'B.Com', 'B.Sc.', 'M.Sc.', 'BBA',
    'BCA', 'MCA', 'MBBS', 'BDS', 'MD', 'MS', 'Diploma', 'Certification',
    'BE', 'BA', 'MA', 'BEd', 'MEd', 'BArch', 'MArch', 'Pharm.D', 'Pharmaceutical',
    'PG Diploma', 'D.Eng.', 'DSc', 'D.Phil', 'D.Litt', 'D.D.S.', 'D.V.M.', 'D.Pharm'
]

def extract_education(input_text):
    input_text = input_text.replace('\n',' ')
    input_text = input_text.replace('\t',' ')
    # print(input_text)
    
    tokens = input_text.split(' ')
    degrees = []

    for token in tokens:
        if token in QUALIFICATIONS:
            degrees.append(token)
        else:
            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token)
            if token in QUALIFICATIONS:
                degrees.append(token)
    

    return degrees