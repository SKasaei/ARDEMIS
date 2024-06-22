import gensim
from py4j.java_gateway import JavaGateway

#for dictionary
from wordhoard import Synonyms

#connecting to java 
gateway = JavaGateway()
Myepsilon = gateway.entry_point.getMyepsilon()
#load EMF or UML model here => Enter name of model
#Myepsilon.importUMLModel("h1")
Myepsilon.importEMFModel("SDG")
#Myepsilon.importEMFModel("uni")

#Enter path of pre-trained model to generate Synonyms like woed2vec or FastText
path='H:/Uni/wiki-news-300d-1M.vec' #EXAMPLE Wiki news
model = gensim.models.KeyedVectors.load_word2vec_format(path)

#getting elements of model (UML or EMF)
print(Myepsilon.getContentsName())
print("\n")
ModelElementsName= Myepsilon.getEName()
print(ModelElementsName)
print("\n")
ModelElementsId= Myepsilon.getEId()
print(ModelElementsId)
print("\n")

print("Starting by pre-trained model")
print("\n")

# checking by pre-trained model
l=0
for k in range(len(ModelElementsName)):
    if ModelElementsName[k] in model.index_to_key:
      b= model.most_similar(ModelElementsName[k],topn=30)
      Myepsilon.clearSimilarwords()
    
      for n in range(len(b)):
        Myepsilon.setSimilarwords(b[n][0].upper())

      Myepsilon.similarWordCheck(ModelElementsName[k].upper(), ModelElementsId[k], "**Pre-trained model**")
    else:
       print(ModelElementsName[k] + 'is not in vocab \n')

print("\n")
print("Starting by Dictionary")
print("\n")

# checking by Dictionary
l=0
for k in range(len(ModelElementsName)):
      print(ModelElementsName[k])
      print("\n")
      b= Synonyms(search_string=ModelElementsName[k].lower(), output_format='list',  sources = ['merriam-webster', 'synonym.com', 'thesaurus.com', 'wordnet']).find_synonyms()
      if isinstance(b, list):
        Myepsilon.clearSimilarwords()
        for n in range(len(b)):
            Myepsilon.setSimilarwords(b[n].upper())
        Myepsilon.similarWordCheck(ModelElementsName[k].upper(), ModelElementsId[k], "**Dictionary**")
      else:
        print(ModelElementsName[k] + ' is not in vocab \n')