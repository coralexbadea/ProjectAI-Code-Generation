import pandas as pd
from api import getCodexSolving
import csv
import re 

def currateSolving(solving):
	result = []
	solving = re.sub("([/\n]+)","\n",solving)
	for line in solving.split("\n"):
		if '#' not in line and "\\" not in line:
			result += [line]
	
	return "\n".join(result)

def createCodexFile(textFile="./katas_csv", targetFile="./kata_dataset"):
	df = pd.read_csv(textFile)
	f = open(targetFile, 'a')
	
	length = len(df["description"])
	index = 0
	for text in df["description"]:
		text = text[:150] if len(text) >= 150 else text
		prompt = f"\"\"\"\n{text}\n\"\"\""
		solving = getCodexSolving(prompt)
		solving = currateSolving(solving)
		solving = solving[:5000] if len(solving) >= 5000 else solving
		f.write(f"\n# {text}\n")
		f.write(solving)
		print(f"{index}/{length}")
		index += 1
	f.close()
	
def createCodexCsv(textFile="./katas_csv",targetCSV="./kata_dataset_csv" ,targetFile="./english_python_data.txt"):
	
	target = open(targetCSV, 'a')
	writer = csv.writer(target)
	#header = ["code", "description", "codex"]
	#writer.writerow(header)
	
	df = pd.read_csv(textFile)
	f = open(targetFile, 'a')
	
	length = len(df["description"][2305:])
	index = 2305
	for text in df["description"]:
		text = text[:250] if len(text) >= 250 else text
		prompt = f"\"\"\"\n{text}\n\"\"\""
		solving = getCodexSolving(prompt)
		solving = currateSolving(solving)
		solving = currateSolving(solving)
		solving = solving[:500] if len(solving) >= 500 else solving
		f.write(f"\n# {text}\n")
		f.write(solving)
		
		data = [df["code"][index], text, solving]
		writer.writerow(data)
		
		print(f"{index}/{length}")
		index += 1
	f.close()
	target.close()
	
		
if __name__ == "__main__":
	createCodexCsv()
	
