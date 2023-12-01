
import requests
from bs4 import BeautifulSoup

def create_dictionary_from_url(url):

    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    result_dict = {}

    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    for heading in headings:
        
        heading_text = heading.get_text(strip=True)

        # Find the next heading
        next_heading = heading.find_next(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        content = []
        current_element = heading.find_next(['p', 'ul', 'ol'])
       
        while current_element and current_element != next_heading and not current_element.name.startswith('h'):
            current = current_element.get_text(strip=True)
            cleaned_text = current.replace('\xa0', ' ')
            # import pdb
            # pdb.set_trace()
            content.append(cleaned_text)

            current_element = current_element.find_next(['p', 'ul', 'ol', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        content = [c for c in content if c]

        result_dict[heading_text] = content

    return result_dict

def main(list_of_routes):
    qna_data = {}
    
    
    for each in list_of_routes:
        website_url = f'https://help.assetpanda.com/{each}.html'
        ans = create_dictionary_from_url(website_url)
        for key, value in ans.items():
            qna_data[key] = value
    return qna_data







list_of_routes = ['Adding_and_Editing_Groups','Delete_Groups','where_to_begin']
qna_data = main(list_of_routes)



import pprint
pprint.pprint(qna_data)






