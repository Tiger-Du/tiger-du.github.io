import json

with open('./_build/html/embeddings.json', 'r') as file:
    json_data = json.load(file)
    json_data['Kind'] = "Article"

with open('./_build/html/embeddings.json', 'w') as file:
    file.write(json.dumps(json_data))
