import sys
import inference

embs,sen=inference.prepare_embs()
rel=inference.inference_from_embs(embs,sen)
y_=inference.knn_treat(rel)
inference.inference_after_knn(y_,sen)

