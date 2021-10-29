

import Levenshtein
import pandas
import tqdm
import extension


'''
請輸入一個搜尋字，從資料表中找出距離比較近的搜尋字，並將分數顯示出來。
'''


word = "covid"


tubulation = extension.tubulation(path="resource/csv/data.csv")
tubulation.read()
tubulation.table.dropna(subset=['abstract'], inplace=True)
size = 100
selection = tubulation.table.sample(size, random_state=0)


content = " ".join(selection['abstract'].tolist())
article = extension.article(content=content)
pass

dictionary = {
    'default':extension.dictionary(word=article.get(what='word', normalization='default')),
    'porter':extension.dictionary(word=article.get(what='word', normalization='porter'))
}
table = {
    'default':dictionary['default'].convert(what='word', to='table'),
    'porter':dictionary['porter'].convert(what='word', to='table')
}

group = {
    'word':[],
    'score':[]
}
for iteration, item in table['default'].iterrows():

    group['word'] += [item['word']]
    group['score'] += [Levenshtein.distance(word, item['word'])]
    pass

group = pandas.DataFrame(group).sort_values('score').reset_index(drop=True)
html = group.to_html()



