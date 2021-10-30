

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

