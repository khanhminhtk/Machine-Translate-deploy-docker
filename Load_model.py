import os
from transformers import EncoderDecoderModel, BertTokenizer, pipeline

model_path = os.path.abspath("Model")
en_tokenizer_path = os.path.abspath("tokenizer_en")
vi_tokenizer_path = os.path.abspath("tokenizer_vi")

model = EncoderDecoderModel.from_pretrained(model_path)
en_tokenizer = BertTokenizer.from_pretrained(en_tokenizer_path)
vi_tokenizer = BertTokenizer.from_pretrained(vi_tokenizer_path)
