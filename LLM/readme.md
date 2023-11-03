# LLMs-related dataset

Two files are included: the training set `LLM_train.json` for fine-tuning LLMs and the test set `LLM_test.json` for testing the effect after fine-tuning.

Each sequence has been filled out according to the prompt template given in the paper .

```
{"conversations": [{"from": " human", "value":"input_datainputdata"}, {"from": "gpt", "value":"output_dataoutputdata"}]}
```
