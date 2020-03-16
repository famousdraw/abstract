import sys
sys.path.append('../src')
import inference.py

embs=inference.prepare_embs()
inference.inference_from_embs(embs)
