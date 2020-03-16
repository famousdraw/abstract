#=============================sif_embedding.py
def sif_embedding(sen ):
    import sys
    sys.path.append('../src')
    import data_io, params, SIF_embedding
    import params
    import SIF_embedding
    # input
    wordfile = '../data/dic_files.txt' # word vector file, can be downloaded from GloVe website
    weightfile = '../data/dic_freq.txt' # each line is a word and its frequency
    weightpara = 1e-3 # the parameter in the SIF weighting scheme, usually in the range [3e-5, 3e-3]
    rmpc = 1 # number of principal components to remove in SIF weighting scheme
    #sentences = ['这是一个例句', '这是一个更长一些的例句']
    #sentences = ['昨天天气不错', '这是一个更长一些的例句']
    sentences=sen
    #sentences = ['this is an example sentence', 'this is another sentence that is slightly longer']

    # load word vectors
    (words, We) = data_io.getWordmap(wordfile)
    #print(words,We) #单词，和词向量
    # load word weights
    word2weight = data_io.getWordWeight(weightfile, weightpara) # word2weight['str'] is the weight for the word 'str'
    weight4ind = data_io.getWeight(words, word2weight) # weight4ind[i] is the weight for the i-th word
    # load sentences
    #x, m, _ = data_io.sentences2idx(sentences, words) # x is the array of word indices, m is the binary mask indicating whether there is a word in that location
    x, m  = data_io.sentences2idx(sentences, words) # x is the array of word indices, m is the binary mask indicating whether there is a word in that location
    #print(x,m)
    w = data_io.seq2weight(x, m, weight4ind) # get word weights
    #print('word weight:',w)
    # set parameters
    #params = params.params()
    params = params.params_all()  #name 'params' is not defined
    params.rmpc = rmpc
    # get SIF embedding
    embedding = SIF_embedding.SIF_embedding(We, x, w, params) # embedding[i,:] is the embedding for sentence i
    return embedding

