<h2> project_ratatouille </h2>\n

An automatic random recipe generator made with a custom trained hugging-face's distilGPT2 transformer. Check out their other models as well, pretty cool stuff <a href='https://huggingface.co/models'>Link</a>\n

I've used Eight Portions Recipe Data set which you can get here <a href='https://eightportions.com/datasets/Recipes/'>Link</a>

<h3>Model</h3>
you can directly use this model from the huggingface/transformers library\n\n

tokenizer = AutoTokenizer.from_pretrained("kalki7/distilgpt2-ratatouille")\n
model = AutoModel.from_pretrained("kalki7/distilgpt2-ratatouille")
