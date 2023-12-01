# app.py
import pdfplumber
import re

knowledge_base = None  # Initialize as None

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def clean_text(text):
    #hader
    header_pattern = r"\d{2}/\d{2}/\d{4},\s\d{2}:\d{2}\s.*"
    text = re.sub(header_pattern, "", text)

    # Remove footer 
    footer_pattern = r"https://.*|Page \d+/\d+" 
    text = re.sub(footer_pattern, "", text)

    # Example: remove non-alphanumeric characters
    cleaned_text = re.sub(r'[^\w\s.]', '', text)  
    return cleaned_text

def create_knowledge_base(pdf_path):
    global knowledge_base  # Use the global variable
    text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(text)
    
    # Create a knowledge base, e.g., a dictionary
    knowledge_base = {'pdf_content': cleaned_text}
    

# Check if this script is the main script being run
if __name__ == "__main__":
    pdf_path = "./pdf_path/Create_an_audit.pdf"
    create_knowledge_base(pdf_path)
    print(knowledge_base)


import app
print(app.knowledge_base)




import re

text = ""

# Define a regular expression to match the headings
heading_pattern = re.compile(r'^\s*\d+\.\s*([^\n]+)\n', re.MULTILINE)

# Find all matches in the text
headings = heading_pattern.findall(text)

# Print the extracted headings
for heading in headings:
    print(heading.strip())


