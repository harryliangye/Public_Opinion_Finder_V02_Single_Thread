from django.http import HttpResponseRedirect

def home(request):
	return HttpResponseRedirect('/Search_Engine')