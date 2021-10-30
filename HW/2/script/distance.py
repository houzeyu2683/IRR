

import Levenshtein
import pandas


'''
輸入搜索字，顯示結果數量上限，根據指定的 word frequency 表中去搜尋距離最近的結果。
'''


word = "covid"
top = 20
size = [1000, 5000, 10000, 49788]


summary = []
for s in size:

    table = {
        'default':pandas.read_csv("resource/csv/frequency/{}/default.csv".format(s), na_filter = False),
        'porter':pandas.read_csv("resource/csv/frequency/{}/porter.csv".format(s), na_filter = False)
    }
    group = {
        '{}-word'.format(s):[],
        '{}-score'.format(s):[]
    }
    for iteration, item in table['default'].iterrows():

        group['{}-word'.format(s)] += [item['word']]
        group['{}-score'.format(s)] += [Levenshtein.distance(word, item['word'])]
        pass

    group = pandas.DataFrame(group).sort_values('{}-score'.format(s)).reset_index(drop=True)
    summary += [group.head(top)]
    pass

summary = pandas.concat(summary,axis=1)
response = summary.to_html()

