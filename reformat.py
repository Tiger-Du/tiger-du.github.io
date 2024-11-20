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

    for element in soup.find_all(class_='no-underline text-inherit hover:text-inherit px-2 font-normal select-none transition-opacity opacity-0 focus:opacity-100 group-hover:opacity-70 __WebInspectorHideElement__'):
        element.decompose()

    for element in soup.find_all(class_='flex items-center h-6 mb-5 text-sm font-light __WebInspectorHideElement__'):
        element.decompose()
    
    for element in soup.find_all(class_='theme rounded-full aspect-square border border-stone-700 dark:border-white hover:bg-neutral-100 border-solid overflow-hidden text-stone-700 dark:text-white hover:text-stone-500 dark:hover:text-neutral-800 w-8 h-8 mx-3 __WebInspectorHideElement__'):
        element.decompose()

    for element in soup.find_all(class_='no-underline text-inherit hover:text-inherit ml-2 select-none transition-opacity opacity-0 focus:opacity-100 group-hover:opacity-70'):
        element.decompose()

    for element in soup.find_all(class_='bg-white/80 backdrop-blur dark:bg-stone-900/80 shadow dark:shadow-stone-700 p-3 md:px-8 sticky w-screen top-0 z-30 h-[60px]'):
        element.replace_with('<div class="bg-white dark:bg-stone-900 p-3 md:px-8 sticky w-screen top-0 z-30 h-[60px]"><nav class="flex items-center justify-between flex-nowrap max-w-[1440px] mx-auto"><div class="flex flex-row xl:min-w-[19.5rem] mr-2 sm:mr-7 justify-start items-center shrink-0"><a class="flex items-center ml-3 dark:text-white w-fit md:ml-5 xl:ml-7" href="/"><span class="text-md sm:text-xl tracking-tight sm:mr-5">Information Gain</span></a></div><div class="flex items-center flex-grow w-auto"><div class="flex-grow hidden text-md lg:block"><div class="relative inline-block mx-2 grow-0"><a class="inline-flex items-center justify-center w-full mx-2 py-1 text-md font-medium dark:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75" href="/research">Research</a></div><div class="relative inline-block mx-2 grow-0"><a class="inline-flex items-center justify-center w-full mx-2 py-1 text-md font-medium dark:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75" href="/typography">Typography</a></div><div class="relative inline-block mx-2 grow-0"><a class="inline-flex items-center justify-center w-full mx-2 py-1 text-md font-medium dark:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75" href="/poetry">Poetry</a></div></div><div class="flex-grow block"></div><button class="theme rounded-full aspect-square border border-stone-700 dark:border-white hover:bg-neutral-100 border-solid overflow-hidden text-stone-700 dark:text-white hover:text-stone-500 dark:hover:text-neutral-800 w-8 h-8 mx-3" title="Toggle theme between light and dark mode." aria-label="Toggle theme between light and dark mode."><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" data-slot="icon" class="h-full w-full p-0.5 hidden dark:block"><path fill-rule="evenodd" d="M9.528 1.718a.75.75 0 0 1 .162.819A8.97 8.97 0 0 0 9 6a9 9 0 0 0 9 9 8.97 8.97 0 0 0 3.463-.69.75.75 0 0 1 .981.98 10.503 10.503 0 0 1-9.694 6.46c-5.799 0-10.5-4.7-10.5-10.5 0-4.368 2.667-8.112 6.46-9.694a.75.75 0 0 1 .818.162Z" clip-rule="evenodd"></path></svg><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon" class="h-full w-full p-0.5 dark:hidden"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z"></path></svg></button><div class="block sm:hidden"></div><div class="hidden sm:block"></div></div></nav></div>')

    try:
        file.write(soup.prettify('utf-8'))
    except:
        file.write(str(soup))
