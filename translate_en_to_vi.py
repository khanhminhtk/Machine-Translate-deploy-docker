from Load_model import model, en_tokenizer, vi_tokenizer
import torch

def translate_en_to_vi (sentence):
    inputs = en_tokenizer(sentence, return_tensors="pt")

    with torch.no_grad():
        outputs = model.generate(
            inputs["input_ids"],
            max_length=40,
            num_beams=3,
            early_stopping=True,
            decoder_start_token_id=model.config.decoder_start_token_id
        )
        translated_sentence = vi_tokenizer.decode(outputs[0], skip_special_tokens=True)
        return "".join(translated_sentence)
    
# print(translate_en_to_vi("Many North and Central American species are visited by honey bees, as well as specialist bees that pollinate only a single species."))