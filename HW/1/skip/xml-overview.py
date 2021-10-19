import os
from xml.etree import ElementTree as et
folder = 'hw1_data'
tag = []
for i in os.listdir(folder):

    if('xml' in i):

        x = et.parse(os.path.join(folder, i))
        for j in x.iter():

            tag += [j.tag]
            pass

        pass
    
    pass

len(tag)
len(set(tag))
set(tag)


{
    'PubmedData', 'MeshHeading', 'Title', 'JournalIssue', 
    'Affiliation', 'Keyword', 'MedlinePgn', 'ELocationID', 
    'Minute', 'Author', 'ISSNLinking', 'Day', 'Pagination', 
    'ArticleIdList', 'PublicationType', 'Year', 'NlmUniqueID', 
    'ReferenceList', 'Issue', 'CoiStatement', 'ISSN', 'LastName', 
    'Month', 'PublicationTypeList', 'KeywordList', 'History', 
    'VernacularTitle', 'QualifierName', 'Citation', 
    'PubmedArticleSet', 'PMID', 'Abstract', 'PubDate', 
    'MeshHeadingList', 'Identifier', 'MedlineJournalInfo', 
    'PubMedPubDate', 'Article', 'MedlineTA', 'AbstractText', 
    'MedlineCitation', 'Reference', 'AffiliationInfo', 
    'ArticleDate', 'ISOAbbreviation', 'Language', 'ArticleTitle', 
    'PubmedArticle', 'Journal', 'ForeName', 'Hour', 'DateCompleted', 
    'DescriptorName', 'DateRevised', 'ArticleId', 'Initials', 
    'CitationSubset', 'PublicationStatus', 'Volume', 
    'CopyrightInformation', 'Country', 'AuthorList'
}