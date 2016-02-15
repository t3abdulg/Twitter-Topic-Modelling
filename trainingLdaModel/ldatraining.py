import logging, gensim, bz2

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

id2word = gensim.corpora.Dictionary.load_from_text('wiki_en_wordids.txt_wordids.txt')

mm = gensim.corpora.MmCorpus('wiki_en_wordids.txt_tfidf.mm')

model = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=200, update_every=1, chunksize=10000, passes=1)

model.save('lda.model')

