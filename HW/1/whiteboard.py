

import os, json, pandas, re
from xml.etree import ElementTree as et
import string


class document:

    def __init__(self, folder):
        
        self.folder = folder
        return
    
    def read(self):

        group = {
            'path' : [], 
            'original content': [],
            'character size':[],
            'word size':[],
            'sentence size':[],
        }
        pass

        cache = {}
        
        for index, name in enumerate(os.listdir(self.folder), 1):

            path = os.path.join(self.folder, name)
            group['path'] += [path]
            
            if('xml' in name):

                data = et.parse(path)
                root = data.getroot()

                ##  擷取所有的字串。
                content = "".join([e.text for e in root.iter()])
                group['original content'] += [content]

                text = ""
                for article in root.findall("PubmedArticle"):

                    abstract = article.find("MedlineCitation").find("Article").find("Abstract")
                    text += "".join([e.text for e in abstract.findall("AbstractText")])
                    pass

                character = re.sub(r'[^{}{}{}]+'.format(string.punctuation, string.digits, string.ascii_letters), '', text)
                sentence  = text.split(".")[:-1]
                word = re.sub("\s+", " ", re.sub(r'[{}]+'.format('.,!?:~();'), " ", text)).split(" ")[:-1]
                print(path)
                print(word)
                print("-"*20)
                group['character size'] += [len(character)]
                group['sentence size'] += [len(sentence)]
                group['word size'] += [len(word)]
                pass

            if('json' in name):

                with open(path, 'r') as paper:

                    data = json.load(paper)
                    pass
                
                content = []
                text = []
                for i in data:

                    for k, v in i.items():

                        if(k=='tweet_text'):
                            
                            text += [v]
                            pass

                        content += [v]        
                        pass

                    pass
                
                content = "".join(content)
                text = ''.join(text)
                character = re.sub(r'[^{}{}{}]+'.format(string.punctuation, string.digits, string.ascii_letters),'', text)
                word = re.sub("\s+", " ", re.sub(r'[{}]+'.format('.,!?:~();'), " ", text)).split(" ")
                sentence  = text.split(".")[:-1]
                group['original content'] += [content]
                group['character size'] += [len(character)]
                group['sentence size'] += [len(sentence)]
                group['word size'] += [len(word)] 
                pass
            
            number = index
            pass

        # return(group)
        self.data = pandas.DataFrame(group)
        print("load {} files...".format(number))
        return
    
    def search(self, keyword):

        output = {
            "path":[],
            "exist":[],
            "number":[]
        }
        pass
    
        for _, item in self.data.iterrows():

            output['path'] += [item['path']]
            output['exist'] += [bool(re.search(keyword, item['original content']))]
            output['number'] += [len(re.findall(keyword, item['original content']))]
            pass
        
        output = pandas.DataFrame(output)
        return(output)

    pass


##  指定搜索路徑
doc = document(folder = 'demo_data')
doc.read()
doc.data

##  指定關鍵字搜尋
doc.search(keyword='Covid')


