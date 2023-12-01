import fitz

def scrape(filePath):
    results = [] # list of tuples that store the information as (text, font size, font name) 
    pdf = fitz.open(filePath) # filePath is a string that contains the path to the pdf
    for page in pdf:
        dict = page.get_text("dict")
        print(dict)
        blocks = dict["blocks"]
        for block in blocks:
            if "lines" in block.keys():
                spans = block['lines']
                for span in spans:
                    import pprint
                    data = span['spans']
                    for text in data:
                        # pprint.pprint(text)
                        # print(text)
                        output_dict = {
                            'size': text['size'],
                            'text': text['text']
                        }
                        pprint.pprint(output_dict)
            # print(block['number'])

    pdf.close()
    return results
scrape('/home/dell/Desktop/practice/four_rasa/pdf_path/Create_an_audit.pdf')