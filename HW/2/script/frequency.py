

import extension
import numpy
import os


tubulation = extension.tubulation(path="resource/csv/data.csv")
tubulation.read()
tubulation.table.dropna(subset=['abstract'], inplace=True)


size = [1000, 5000, 10000, 50000]
for s in size:

    if(s):

        selection = tubulation.table.sample(s, random_state=0)
        pass

    else:

        s = len(tubulation.table)
        selection = tubulation.table
        pass


    content = " ".join(selection['abstract'].tolist())
    article = extension.article(content=content)


    dictionary = {
        'default':extension.dictionary(word=article.get(what='word', normalization='default')),
        'porter':extension.dictionary(word=article.get(what='word', normalization='porter'))
    }
    table = {
        'default':dictionary['default'].convert(what='word', to='table').dropna(subset=['word']),
        'porter':dictionary['porter'].convert(what='word', to='table').dropna(subset=['word'])
    }
    table['default']['log frequency'] = numpy.log(table['default']['frequency'])
    table['porter']['log frequency'] = numpy.log(table['porter']['frequency'])
    pass

    link = {}
    link['default'] = "resource/csv/frequency/{}/default.csv".format(s)
    link['porter'] = "resource/csv/frequency/{}/porter.csv".format(s)
    os.makedirs(os.path.dirname(link['default']), exist_ok=True)
    os.makedirs(os.path.dirname(link['porter']), exist_ok=True)
    table['default'].to_csv(link['default'], index=False)
    table['porter'].to_csv(link['porter'], index=False)
    pass




# import asyncio
# import pandas
# import tqdm
# import Levenshtein
# @asyncio.coroutine
# def thread(word, top, size):
#     # size = 1000
#     table = {
#         'default':pandas.read_csv("resource/csv/frequency/{}/default.csv".format(size), na_filter = False),
#         'porter':pandas.read_csv("resource/csv/frequency/{}/porter.csv".format(size), na_filter = False)
#     }
#     group = {
#         'default word({}text)'.format(size):[],
#         'score({}text)'.format(size):[]
#     }    
#     for _, item in tqdm.tqdm(table['default'].iterrows(), total=len(table['default'])):

#         group['default word({}text)'.format(size)] += [item['word']]
#         group['score({}text)'.format(size)] += [Levenshtein.distance(word, item['word'])]
#         pass

#     group = pandas.DataFrame(group).sort_values('score({}text)'.format(size)).reset_index(drop=True)    
#     group = group.head(top)
#     return(group)

# @asyncio.coroutine
# def beta(word, top, size):
#     # size = 1000
#     table = {
#         'default':pandas.read_csv("resource/csv/frequency/{}/default.csv".format(size), na_filter = False),
#         'porter':pandas.read_csv("resource/csv/frequency/{}/porter.csv".format(size), na_filter = False)
#     }
#     group = {
#         'default word({}text)'.format(size):[],
#         'score({}text)'.format(size):[]
#     }    
#     for _, item in tqdm.tqdm(table['default'].iterrows(), total=len(table['default'])):

#         group['default word({}text)'.format(size)] += [item['word']]
#         group['score({}text)'.format(size)] += [Levenshtein.distance(word, item['word'])]
#         pass

#     group = pandas.DataFrame(group).sort_values('score({}text)'.format(size)).reset_index(drop=True)    
#     group = group.head(top)
#     return(group)

# # loop = asyncio.get_event_loop()
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# task = thread(word='covid', top=20, size=50000), beta(word='covid', top=20, size=10000), thread(word='covid', top=20, size=5000), thread(word='covid', top=20, size=1000)
# group = loop.run_until_complete(asyncio.gather(*task))
# summary = [g for g in group]
# # print("func_normal()={a}, func_infinite()={b}".format(**vars()))
# loop.close()