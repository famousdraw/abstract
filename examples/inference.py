#inference.py
import sys
sys.path.append('../src')
sys.path.append('../data')
import sif_embedding
import pre_proc
import numpy as np
def prepare_embs():
    i=0
    sentences=[]
    with open ('../data/test_news.txt','r',encoding='utf=8') as input:
        if i ==0:title_article=input.readline()
        new_article=input.read()
    title_article=''.join(pre_proc.token(title_article))
    print('title_article:',title_article)
    #print(new_article)    
    #body_article=new_article
    #print('body_article:',body_article)
    sentences.append(title_article)
    sentences+=pre_proc.token(new_article)
    #print(sentences)
    body_article=''.join(pre_proc.token(new_article))
    #print(body_article)
    sentences.append(body_article)
    #print(sentences)  #sentences的内容：0：标题  1,2,3,...：内容  最后一条：新闻全部内容
    embs=sif_embedding.sif_embedding(sentences)
    return embs,sentences

def cosine_similarity(u,v):
    """
    Cosine similarity reflects the degree of similarity
    Arguments:
    u -- a word vector of shape (n,)
    v -- a word vector of shape (n,)
    """
    
    distance = 0.0
    # Compute the dot product between u and values
    dot = np.dot(u.T,v)
    # Compute the L2 norm of u
    norm_u = np.sqrt(np.sum(u**2))
    # Compute the L2 norm of v
    norm_v = np.sqrt(np.sum(v**2))
    #Compute the cosine similarity defined by fomula
    cosine_similarity = dot/(norm_u * norm_v)
    return cosine_similarity
 
#V_s 句子向量
#V_t 标题向量
#V_c 文章所有句子总和的向量
#求解相关度的函数
def relevancy_to_article(V_s,V_t,V_c): 
    return (0.5*cosine_similarity(V_s,V_t)+0.5*cosine_similarity(V_s,V_c))


def inference_from_embs(embs,sen):
    from operator import itemgetter, attrgetter
    rel=[]
    sentences=sen
    for i in range(len(sentences)-1):
        #print(i)
        rel.append( (i,abs(relevancy_to_article(embs[i],embs[0],embs[-1]))))
    rel_sorted=sorted(rel, key=itemgetter(1), reverse=True)
    k=0
    #print(rel_sorted)
    result_rel=[]
    for i in range(len(rel_sorted)):
        if k==40:break
        k+=1
        result_rel.append(rel_sorted[i])

    k==0
    result_rel.sort(key=itemgetter(0))
    #print(result_rel)   
    output=[]
    #print(sentences[:-2])
    for i,value in result_rel:
        output.append(sentences[i])
    #print(output)
    return rel

def knn_treat(rel):
    print(__doc__)
    rel=rel
    # Author: Alexandre Gramfort <alexandre.gramfort@inria.fr>
    #         Fabian Pedregosa <fabian.pedregosa@inria.fr>
    #
    # License: BSD 3 clause (C) INRIA


    # #############################################################################
    # Generate sample data
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import neighbors

    np.random.seed(0)
    #X = np.sort(5 * np.random.rand(40, 1), axis=0)

    #T = np.linspace(0, 5, 500)[:, np.newaxis]
    #y = np.sin(X).ravel()


    # Add noise to targets
    #y[::5] += 1 * (0.5 - np.random.rand(8))

    X=[]
    y=[]
    for i,j in rel:
        X.append([i])
        y.append([j])
    T=X

    # #############################################################################
    # Fit regression model
    n_neighbors = 3

    #for i, weights in enumerate(['uniform', 'distance']):
    for i, weights in enumerate(['uniform']):
        knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
        y_ = knn.fit(X, y).predict(T)

        #plt.subplot(2, 1, i + 1)
        #plt.scatter(X, y, color='darkorange', label='data')
        #plt.plot(T, y_, color='navy', label='prediction')
        #plt.axis('tight')
        #plt.legend()
        #plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors,
        #                                                            weights))

    #plt.tight_layout()
    #plt.show()
    return y_

def inference_after_knn(y_,sen):
    y_=y_
    y_reshape=y_.reshape(-1,)
    sentences=sen
    from operator import itemgetter, attrgetter
    rel=[]
    rel_sorted=[]
    for i in range(len(sentences)-1):
        #print(i)
        rel.append( (i,y_reshape[i]))
    rel_sorted=sorted(rel, key=itemgetter(1), reverse=True)
    k=0
    #print(rel_sorted)
    result_rel=[]
    for i in range(len(rel_sorted)):
        if k==40:break
        k+=1
        result_rel.append(rel_sorted[i])

    k==0
    result_rel.sort(key=itemgetter(0))
    #print(result_rel)   
    output=[]
    print(sentences[:-2])
    for i,value in result_rel:
        output.append(sentences[i])
    print(output)


