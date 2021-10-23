import os
import openai
import json

openai.api_key = "PRIVATE_API_KEY"

def getCodexSolving(text, max_tok=1010):
	response = openai.Completion.create(
	  engine="davinci-codex",
	  prompt=text,
	  temperature=0,
	  max_tokens=max_tok,
	  top_p=1,
	  frequency_penalty=1,
	  presence_penalty=0
	)
	return response["choices"][0]["text"]
