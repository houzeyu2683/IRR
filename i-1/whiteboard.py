

from xml.etree import ElementTree as et


class document:

    def __init__(self, path, format):

        self.path = path
        self.format = format
        pass

    def parse(self):

        if(self.format=='xml'):
    
            self.objective = et.parse(self.path)
            pass

        pass
    
    def get(self, what='string', plan="a"):

        if(self.format=='xml'):

            if(what=='string'):

                if(plan=='a'):

                    ##  啥都不管，將所有 element 中的字串提取出來。
                    root = self.objective.getroot()
                    string = "".join([element.text for element in root.iter()])
                    self.string = string
                    pass
                
                if(plan=='b'):
                    
                    ##  假設一篇檔案只包含一篇文章資訊，定義 string 內容為摘要 <Abstract> 中的文字。
                    root = self.objective.getroot()
                    abstract = root.find("PubmedArticle").find("MedlineCitation").find("Article").find("Abstract").findall("AbstractText")
                    string = "".join([element.text for element in abstract])
                    self.string = string
                    pass

                pass

            pass

        pass

    pass
