import sys
import inference
def test():
    embs,sen=inference.prepare_embs()
    rel=inference.inference_from_embs(embs,sen)
    y_=inference.knn_treat(rel)
    return(inference.inference_after_knn(y_,sen))

