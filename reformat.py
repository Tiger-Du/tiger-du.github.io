import json

from bs4 import BeautifulSoup
import lxml

with open('./_build/html/embeddings.json', 'r') as file:
    json_data = json.load(file)
    json_data['Kind'] = "Article"

with open('./_build/html/embeddings.json', 'w') as file:
    file.write(json.dumps(json_data))

with open('./_build/html/embeddings.html', 'r+') as file:
    soup = BeautifulSoup(file, 'lxml')

    for element in soup.find_all(class_='inline-block mr-1'):
        element.decompose()
