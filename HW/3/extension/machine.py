

import gensim


class machine:

    def __init__(self, sentence):

        self.sentence = sentence
        pass

    def build(self, by='CBOW'):

        if(by=='CBOW'):

            self.model = gensim.models.Word2Vec(min_count=1, window=5, sg=0, vector_size=50, epochs=5, seed=0)
            self.model.build_vocab(self.sentence)
            self.model.train(self.sentence, total_examples=self.model.corpus_count, epochs=self.model.epochs)
            pass
        
        if(by=='SG'):

            self.model = gensim.models.Word2Vec(min_count=1, window=5, sg=1, vector_size=50, epochs=5, seed=0)
            self.model.build_vocab(self.sentence)
            self.model.train(self.sentence, total_examples=self.model.corpus_count, epochs=self.model.epochs)
            pass
        
        pass

    pass


        
# model = gensim.models.Word2Vec(min_count=5, window=5, sg=0, vector_size=50, epochs=20, seed=0)
# model.build_vocab(tabulation.sentence)
# model.train(tabulation.sentence, total_examples=model.corpus_count, epochs=model.epochs)