

import numpy
import pandas


class weight:

    def __init__(self, matrix):

        self.matrix = matrix.iloc[:,1:].to_numpy()
        self.term = matrix.iloc[:,0].tolist()
        self.document = matrix.iloc[:,1:].columns.tolist()
        return

    def transform(self, what='tf-idf'):

        if(what=='tf'):

            matrix = pandas.DataFrame(self.matrix)
            matrix.columns = self.document
            matrix.index = self.term
            pass

        if(what=='tf-idf'):

            matrix = numpy.dot(
                self.matrix.transpose(), 
                numpy.diag(numpy.log(self.matrix.shape[1] / (self.matrix > 0).sum(axis=1)))
            )
            matrix = pandas.DataFrame(matrix).transpose()
            matrix.columns = self.document
            matrix.index = self.term
            pass

        if(what=='norm-tf-idf'):

            matrix = self.matrix.copy()
            for i, w in enumerate(matrix.sum(axis=0)):

                matrix[:,i] = matrix[:,i] / w 
                pass

            matrix = numpy.dot(
                matrix.transpose(), 
                numpy.diag(numpy.log(matrix.shape[1] / (matrix > 0).sum(axis=1)))
            )
            matrix = pandas.DataFrame(matrix).transpose()
            matrix.columns = self.document
            matrix.index = self.term
            pass

        return(matrix)

    pass
