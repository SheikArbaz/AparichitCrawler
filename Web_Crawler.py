import urllib
def get_page(url):
        try:
            f = urllib.urlopen(url)
            page = f.read()
            f.close()
            return page
        except:
            return ""
        return ""
def get_next_target(page):
        start_link = page.find('<a href=')
        if start_link == -1:
            return None, 0
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote
def union(p,q):
        for e in q:
            if e not in p:
                p.append(e)
def get_all_links(page):
        links = []
        while True:
            url,endpos = get_next_target(page)
            if url:
                links.append(url)
                page = page[endpos:]
            else:
                break
        return links
def add_to_index(index,keyword,url):#adding url if keyword is already else new element as keyword and url
	for i in index:
		if(i[0]==keyword):
			i[1].append(url)
			return
	index.append([keyword,[url]])
def lookup(index,keyword):#returns list of urls for the given keyword
	for i in index:
		if(i[0]==keyword):
			return i[1]
	return []
def add_page_to_index(index,url,content):#content of the page...so take keywords from content and update the index with keywords and url
	words=content.split()
	for word in words:
		add_to_index(index,word,url)
def crawl_web(seed):
	to_crawl=[seed]
	crawled=[]
	#index=[]
	while to_crawl:
		page=to_crawl.pop()
		if page not in crawled:
			content=get_page(page)
			print "page:- "+page
			print "Content:-" + content
			#add_page_to_index(index,page,content)
			union(to_crawl,get_all_links(content))
			crawled.append(page)
	return crawled
crawled=crawl_web('https://www.udemy.com/')
print "Crawled:-"
for _ in crawled:
	print _
"""print "index:-"
for _ in index:
	print _"""
