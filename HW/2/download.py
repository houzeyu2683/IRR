

##
##  The packages.
from selenium import webdriver
import pandas, os, time, tqdm
import re
import time


##
##  The arguments.
keyword  = 'b'
platform = "pubmed"
site   = "https://pubmed.ncbi.nlm.nih.gov/"
number = 10
folder = "resource/txt/{}".format(keyword)
os.makedirs(folder) if not os.path.isdir(folder) else None


##
##
option = webdriver.chrome.options.Options()
option.binary_location = "/usr/bin/google-chrome"
driver = webdriver.Chrome(options=option, executable_path='driver/chrome')
page = range(1, number+1, 1)
group = {
    "link":[],
    "title":[],
    "abstract":[],
    "tag":[],
    "author":[]
}
for p in page:

    driver.get("{}?term={}&filter=simsearch1.fha&page={}".format(site, keyword, p))
    group['link'] += [i.get_attribute("href") for i in driver.find_elements_by_css_selector(".docsum-title")]
    pass


def remove(x, what=""):

    output = []
    for i in x:

        if(i==what):

            continue

        else:

            output += [i]
            pass

        pass
    
    return(output)


for l in tqdm.tqdm(group['link'], total=len(group['link'])):

    driver.get(l)
    title = driver.find_element_by_css_selector(".heading-title").text
    abstract = driver.find_element_by_css_selector("#enc-abstract p").text
    try:

        tag = driver.find_element_by_css_selector("#enc-abstract+ p").text.split(": ")[-1]
        pass

    except:

        tag = None
        pass

    author = ";".join(remove([i.text for i in driver.find_elements_by_css_selector(".full-name")], what=''))
    group['title'] += [title]
    group['abstract'] += [abstract]
    group['tag'] += [tag]
    group['author'] += [author]
    pass

driver.close()


table = pandas.DataFrame(group)
table.to_csv(os.path.join(folder, "{}.csv".format(keyword)), index=False)
