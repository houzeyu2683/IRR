
import pandas
import tqdm
import itertools
import re
from collections import Counter

class tabulation:

    def __init__(self, path):

        self.path = path
        pass
    
    def read(self):

        self.table = pandas.read_csv(self.path)
        pass
    
    pass
