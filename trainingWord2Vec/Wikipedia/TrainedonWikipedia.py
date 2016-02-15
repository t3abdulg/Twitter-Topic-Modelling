from gensim.models import Word2Vec

model = Word2Vec.load("en.model")

print model.similarity('woman','man')