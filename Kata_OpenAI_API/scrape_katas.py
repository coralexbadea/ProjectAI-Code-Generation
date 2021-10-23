from bs4 import BeautifulSoup 
import requests
import re
import csv

def getKataIds(url="https://www.codewars.com/kata/latest"):
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

	response = requests.get(url, headers=headers)

	soup = BeautifulSoup(response.content, 'html.parser')

	links = []
	for link in soup.find_all('a', href=True):
		if "/kata/" in link["href"]: 
			res = re.search('kata/(.*)/train', str(link))
			if res:
				links += [res.group(1)]
	ids = list(set(links))
	return ids
	
	
def getKataDescriptions(codes):
	texts = []
	for code in codes:
		url = f'https://www.codewars.com/api/v1/code-challenges/{code}'
		res = requests.get(url).json()
		text = res["description"].split("#")[0]
		index = 1
		while(len(text) < 10):
			text = res["description"].split("#")[index]
			index += 1
		text = text.replace('\n', ' ')
		text = re.sub("(if[:|-][^\s]+)","",text)
		text = re.sub("(http[^\s]+)","",text)
		text = text.replace("`", '')
		text = re.sub("([\s]+)"," ",text)
		texts += [text]
	return texts
		
"""
Users the above two functions to get all the latest katas and puts their text into a csv
having the id the respective kata code/id 
"""	
def putKatasInFile(filepath="./katas_csv"):
	f = open(filepath, 'w')
	writer = csv.writer(f)
	header = ["code", "description"]
	writer.writerow(header)

	no_pages = 236 # no_katas / 30_kats_per_page
	url = "https://www.codewars.com/kata/latest"
	for i in range(no_pages):
		pageUrl = url + f"?page={i}"
		ids = getKataIds(pageUrl)
		texts = getKataDescriptions(ids)
		for j in range(len(texts)):
			if(texts[j]):
				data = [ids[j], texts[j]]
				writer.writerow(data)
		print(i, "DONE")
	f.close()


if __name__ == "__main__":
	putKatasInFile()
