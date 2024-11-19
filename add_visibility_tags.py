from glob import glob

import nbformat as nbf

notebooks = glob("./*.ipynb", recursive=True)

text_search_dict = {
    "# remove-cell": "remove-cell",
    "# remove-input": "remove-input",
    "# remove-output": "remove-output",
}

for ipath in notebooks:
    notebook = nbf.read(ipath, nbf.NO_CONVERT)

    for cell in notebook.cells:
        cell_tags = cell.get('metadata', {}).get('tags', [])
        for key, val in text_search_dict.items():
            if key in cell['source']:
                if val not in cell_tags:
                    cell_tags.append(val)
        if len(cell_tags) > 0:
            cell['metadata']['tags'] = cell_tags

    nbf.write(notebook, ipath)
  