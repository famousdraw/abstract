#inference.py
import sys
sys.path.append('../src')
sys.path.append('../data')
import sif_embedding

def prepare_embs():
    i=0
    sentences=[]
    with open ('../data/test_news.txt','r',encoding='utf=8') as input:
        if i ==0:title_article=input.readline()
    new_article=input.read()
    title_article=''.join(token(title_article))
    print('title_article:',title_article)
    #print(new_article)    
    #body_article=new_article
    #print('body_article:',body_article)
	sentences.append(title_article)
    sentences+=token(new_article)
    #print(sentences)
    body_article=''.join(token(new_article))
    #print(body_article)
    sentences.append(body_article)
    #print(sentences)  #sentences的内容：0：标题  1,2,3,...：内容  最后一条：新闻全部内容
    embs=sif_embedding(sentences)
    return embs

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


def infrence_from_embs(embs):
    from operator import itemgetter, attrgetter
    rel=[]
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
    print(sentences[:-2])
    for i,value in result_rel:
        output.append(sentences[i])
    print(output)





