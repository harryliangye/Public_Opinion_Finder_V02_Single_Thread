import requests
from lxml import etree
from urllib.parse import urlparse
from collections import deque

#:queue_url  queue, 
#:added_url  set, 
#:search_results list, 
class Spider:
    def __init__(self, queue_url, added_url, search_results):
        self.current_message_no = len(search_results)
        self.queue_url = queue_url
        self.added_url = added_url
        self.search_results = search_results

    def Crawl(self, nome):
        while(self.queue_url and self.current_message_no < nome):
            url = self.queue_url.popleft()
            self.search_results.append(url)
            page_sc = requests.get(url)
            tree_page = etree.HTML(page_sc.text)
            self.GetUrls(url, tree_page)
            self.current_message_no += 1

    def GetUrls(self, url, tree_page):
    #get urls from the given page and add them into the global g_queque and modify the visited url
    #(page must be parsed #into a tree structure with lxml)
        hrefs = tree_page.xpath("//a/@href")
        for href in hrefs:
            if(href[0:4] != "http"):
                href = self.RootDomainOf(url) + href
    #if this url is not visited, append it into the BFS queue
            if(not(href in self.added_url)):
                self.added_url.add(href)
                self.queue_url.append(href)

    def RootDomainOf(self,url):
        parsed_url = urlparse(url)
        return parsed_url.scheme+"://"+ parsed_url.netloc