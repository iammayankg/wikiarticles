import wikipedia
import codecs
import os
import datetime
topic = "climate change"
wikipedia.set_lang("en")
wikipedia.set_rate_limiting(True, min_wait=datetime.timedelta(seconds=1))
def writepage(term,direc):
	try:
		termpage=wikipedia.page(term)
		content=termpage.content
		f=codecs.open(direc + "//" + term+".txt","w","utf-8")
		f.write(content)
		f.close()
		return termpage.links
	except Exception as e:
		print(e)
		return []

topics = ['poverty','climate change']
for topic in topics:
	results=wikipedia.search(topic)
	print(results)
	links = []
	os.makedirs(topic)
	for term in results:
		newlink = writepage(term,topic)
		links = links + newlink

	for link in links:
		nl=writepage(link,topic)
