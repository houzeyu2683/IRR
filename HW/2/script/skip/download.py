

##  The packages.
from selenium import webdriver
import pandas, os, tqdm, time


'''
為了演示作業二的 zipf 分佈，會需要事前下載一定數量的文本資料，
以下針對 "pubmed" 網站進行文章摘要下載。
'''


##  The arguments before get the text data.
keyword  = 'COVID-19'
platform = "pubmed"
site   = "https://pubmed.ncbi.nlm.nih.gov/"
number = 50
folder = "resource/csv/{}".format(keyword)
os.makedirs(folder) if not os.path.isdir(folder) else None


##  Get the urls of article.
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


##  Convert the links to the table.
link = pandas.DataFrame({"link":group['link']})
link.to_csv(os.path.join(folder, "link.csv"), index=False)


##  Remove the "" in the list.
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


##  Get the information base on links.
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




##  Convert the information to table.
table = pandas.DataFrame(group)
table.to_csv(os.path.join(folder, "{}.csv".format(keyword)), index=False)
driver.close()