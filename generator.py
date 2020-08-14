from transformers import AutoTokenizer,AutoModelForCausalLM
import pandas as pd

tokenizer = AutoTokenizer.from_pretrained('kalki7/distilgpt2-ratatouille')
model = AutoModelForCausalLM.from_pretrained('kalki7/distilgpt2-ratatouille')

prompt_text='Ingredients: \n'
encoded_prompt=tokenizer.encode(
prompt_text,
add_special_tokens=False,
return_tensors='pt')

op_seq=model.generate(
    input_ids=encoded_prompt,
    max_length=1000,
    temperature=0.9,
    top_k=20,
top_p=0.9,
repetition_penality=1,
do_sample=True,
num_return_sequences=1)

op_seq[0]
print(tokenizer.decode(op_seq[0]))
