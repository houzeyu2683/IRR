import os
import re 
from xml.etree import ElementTree as et

path = 'hw1_data/test1.xml'
archive  = et.parse(path)
for i in archive.getroot().iter():

    print(i.tag)
    print(set(i.text))
    print("-"*20)
    pass

# bool(re.search("[ \n]", "\n "))


# 針對每個文件都要有疑