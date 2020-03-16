import sys
import inference

embs,sen=inference.prepare_embs()
inference.inference_from_embs(embs,sen)
