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

    for element in soup.find_all(class_='no-underline text-inherit hover:text-inherit px-2 font-normal select-none transition-opacity opacity-0 focus:opacity-100 group-hover:opacity-70'):
        element.decompose()

    for element in soup.find_all(class_='flex items-center h-6 mb-5 text-sm font-light'):
        element.decompose()
    
    for element in soup.find_all(class_='theme rounded-full aspect-square border border-stone-700 dark:border-white hover:bg-neutral-100 border-solid overflow-hidden text-stone-700 dark:text-white hover:text-stone-500 dark:hover:text-neutral-800 w-8 h-8 mx-3'):
        element.decompose()

    for element in soup.find_all(class_='no-underline text-inherit hover:text-inherit ml-2 select-none transition-opacity opacity-0 focus:opacity-100 group-hover:opacity-70'):
        element.decompose()

    for element in soup.find_all(class_='bg-white/80 backdrop-blur dark:bg-stone-900/80 shadow dark:shadow-stone-700 p-3 md:px-8 sticky w-screen top-0 z-30 h-[60px]'):
        element.replace_with('<div class="bg-white dark:bg-stone-900 p-3 md:px-8 sticky w-screen top-0 z-30 h-[60px]"><nav class="flex items-center justify-between flex-nowrap max-w-[1440px] mx-auto"><div class="flex flex-row xl:min-w-[19.5rem] mr-2 sm:mr-7 justify-start items-center shrink-0"><a class="flex items-center ml-3 dark:text-white w-fit md:ml-5 xl:ml-7" href="/"><span class="text-md sm:text-xl tracking-tight sm:mr-5">Information Gain</span></a></div><div class="flex items-center flex-grow w-auto"><div class="flex-grow hidden text-md lg:block"><div class="relative inline-block mx-2 grow-0"><a class="inline-flex items-center justify-center w-full mx-2 py-1 text-md font-medium dark:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75" href="/research">Research</a></div><div class="relative inline-block mx-2 grow-0"><a class="inline-flex items-center justify-center w-full mx-2 py-1 text-md font-medium dark:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75" href="/typography">Typography</a></div><div class="relative inline-block mx-2 grow-0"><a class="inline-flex items-center justify-center w-full mx-2 py-1 text-md font-medium dark:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75" href="/poetry">Poetry</a></div></div><div class="flex-grow block"></div><div class="block sm:hidden"></div><div class="hidden sm:block"></div></div></nav></div>')
    
    try:
        file.write(str(soup))
    except:
        file.write(soup.prettify('utf-8'))

with open('./_build/html/embeddings.html', 'r') as file:
    soup = BeautifulSoup(file, 'lxml')

    soup
