

##
##  The packages.
from selenium import webdriver
import pandas, os, tqdm, time

'''
內科 Internal Medicine
胃腸科 Gastroenterology
心臟內科 Cardiology
新陳代謝科 Metabolism
感控科 Infection Control
腎臟科 Nephrology
神經內科 Neurology
胸腔內科 Chest Medicine
外科 Surgery
胸腔外科 Thoracic Surgery
'''


##
##  The arguments.
keyword  = 'Orthopedics'
platform = "pubmed"
site   = "https://pubmed.ncbi.nlm.nih.gov/"
number = 50
folder = "resource/txt/{}".format(keyword)
os.makedirs(folder) if not os.path.isdir(folder) else None


##
##
option = webdriver.chrome.options.Options()
option.binary_location = "/usr/bin/google-chrome"
# option.add_argument('--no-sandbox')
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

link = pandas.DataFrame({"link":group['link']})
link.to_csv(os.path.join(folder, "link.csv"), index=False)

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
    try:
        
        abstract = driver.find_element_by_css_selector("#enc-abstract p").text
        pass

    except:

        abstract = None
        pass

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
    time.sleep(0.8)
    pass





table = pandas.DataFrame(group)
table.to_csv(os.path.join(folder, "{}.csv".format(keyword)), index=False)
driver.close()