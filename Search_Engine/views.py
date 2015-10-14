from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template.context_processors import csrf
from Search_Engine.models import Entry_Linkpool
from django.utils import timezone
from .crawler import Spider
from _collections import deque
#Begin-------------------------------------Server-Initialization------------------------------------Begin#
g_memory_pointer = 0
g_runtime_memory = []

class Search_Scene:
	def __init__(self,usrid):
		self.page = 0
		self.usr_id = usrid
		self.queue_url = deque([])
		self.added_url = set([])
		self.search_results = []

for g_memory_pointer in range(0,100):
	new_scene = Search_Scene(-1)
	g_runtime_memory.append(new_scene)
#End---------------------------------------Server-Initialization--------------------------------------End#
def home_page(request):
	request.session['visitor_id'] = 0
	return render(request,'Search_Engine/home_page.html')

	
def find(request):
	if(request.session.get('visitor_id') == 0):
		return_id = AllocateNewMemory()
	else:
		return_id = request.session.get('visitor_id')
	request.session['visitor_id'] = return_id
	if('P' in request.POST):
		action = -1
	else:
		action = 0

	(page,search_results) = UsrReqPro(return_id, action)
	request.session['visitor_id'] = return_id


	return render(request, 'Search_Engine/find.html', {'page':page,'result_list':search_results})

def UsrReqPro(return_id, action):
	#type == 1 : next, type == 0 : previous
	global g_runtime_memory
	for usr in range(0,100):
		if(return_id == g_runtime_memory[usr].usr_id):
			if(action == -1):
				g_runtime_memory[usr].page -= 1
				return (g_runtime_memory[usr].page, g_runtime_memory[usr].search_results[((g_runtime_memory[usr].page - 1)* 20) : (g_runtime_memory[usr].page * 20)])	
			else:
				if(len(g_runtime_memory[usr].search_results) < 20 * (g_runtime_memory[usr].page + 1)):
					spider = Spider(g_runtime_memory[usr].queue_url,g_runtime_memory[usr].added_url, g_runtime_memory[usr].search_results)
					spider.Crawl((g_runtime_memory[usr].page + 1) * 20)
				g_runtime_memory[usr].page += 1
				return (g_runtime_memory[usr].page, g_runtime_memory[usr].search_results[((g_runtime_memory[usr].page - 1)* 20) : (g_runtime_memory[usr].page * 20)])
	return None

def AllocateNewMemory():
	global g_runtime_memory
	global g_memory_pointer
	entry_urls = []
	g_runtime_memory[(g_memory_pointer % 100)].usr_id = g_runtime_memory[((g_memory_pointer - 1) % 100)].usr_id + 100
	g_runtime_memory[(g_memory_pointer % 100)].page = 0
	g_runtime_memory[(g_memory_pointer % 100)].queue_url = deque([])
	g_runtime_memory[(g_memory_pointer % 100)].added_url = set([])
	g_runtime_memory[(g_memory_pointer % 100)].search_results = []
	entry_urls = Entry_Linkpool.objects.all()
	for url in entry_urls:
		g_runtime_memory[(g_memory_pointer % 100)].queue_url.append(url.link)
		g_runtime_memory[(g_memory_pointer % 100)].added_url.add(url.link)
		print(url)
	g_memory_pointer += 1
	return g_runtime_memory[((g_memory_pointer - 1) % 100)].usr_id
# Create your views here.
