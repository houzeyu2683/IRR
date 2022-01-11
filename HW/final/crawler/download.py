
##  The packages.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
import pandas, os, tqdm, time

site   = "https://www.ncbi.nlm.nih.gov/research/coronavirus/"
option = webdriver.chrome.options.Options()
option.binary_location = "/usr/bin/google-chrome"
driver = webdriver.Chrome(options=option, service=Service('driver/chrome'))


##  Script.
keyword  = ["alzheimer", "bald", "medicine", "rash", "vaccine"]
for k in keyword:
    
    table = pandas.read_csv("./{}.tsv".format(k), sep='\t')
    table = table.iloc[0:100,:].reset_index(drop=True)
    table['abstract'] = None
    for iteration, index in enumerate(table['pmid']):
        
        driver.get(site)
        driver.find_element(By.CSS_SELECTOR, ".ng-valid").send_keys(index)
        driver.find_element(By.CSS_SELECTOR, ".search-btn").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".publication-title").click()
        time.sleep(2)
        abstract = driver.find_element(By.CSS_SELECTOR, ".content").text
        table.at[iteration,'abstract'] = abstract
        pass

    pass
    os.makedirs("csv/", exist_ok=True)
    table.to_csv('csv/{}.csv'.format(k), index=False)
    pass



