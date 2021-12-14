
import re
from termcolor import colored

def mark(title=None, content=None, sentence=None):

    # title = colored(title, 'blue')
    title = "\33[44m" + title + '\33[0m'
    for s in sentence:

        content = content.replace(s, "\33[33m" + s + "\33[0m")
        pass

    print(title)
    print(content)
    print("-"*50)
    return


# c = 'Objective: We investigated whether implantation of polylactic acid and epsilon-caprolactone copolymer (PLAC) cubes with or without basic fibroblast growth factor (b-FGF) released slowly from gelatin microspheres was able to induce fibrous tissue in the dead space remaining after pneumonectomy in the thoracic cavity.'
# s = 'Objective: We investigated whether implantation of polylactic acid and epsilon-caprolactone copolymer (PLAC) cubes with or without basic fibroblast growth factor (b-FGF) released slowly from gelatin microspheres was able to induce fibrous tissue in the dead space remaining after pneumonectomy in the thoracic cavity.'

# print(c.replace(s, "\33[33m" +s+ "\33[0m"))

