# Project Title: Resume and Email Analyzer

## Overview

The Resume and Email Analyzer is a GUI application built with Python's Tkinter library and Natural Language Processing (NLP) techniques. This application leverages Named Entity Recognition (NER) to extract and recognize information from multiple resumes and emails. It identifies key details such as skills, phone numbers, and other relevant entities.

## Features

- **Multiple Document Analysis**: Analyze multiple resumes and emails simultaneously.
- **Named Entity Recognition (NER)**: Extract and recognize entities like names, phone numbers, and skills from the text.
- **User-Friendly Interface**: Intuitive GUI built with Tkinter for ease of use.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/resume-email-analyzer.git
   cd resume-email-analyzer
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

- Python 3.x
- Tkinter
- spaCy
- pandas
- openpyxl

You can install the required Python packages using the `requirements.txt` file provided.

## Usage

1. **Run the Application**:
   ```bash
   python app.py
   ```

2. **Using the GUI**:
   - **Load Documents**: Click the "Load Documents" button to upload resumes and emails for analysis.
   - **Analyze**: Click the "Analyze" button to process the uploaded documents and extract information.
   - **View Results**: The extracted entities such as names, phone numbers, and skills will be displayed in the GUI.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
