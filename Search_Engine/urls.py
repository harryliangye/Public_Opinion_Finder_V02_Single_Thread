from django.conf.urls import url
from . import views
app_name = 'Search_Engine'
urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
	url(r'^find/$', views.find, name='find'),
]