from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from countries.models import Country
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class HomeView(TemplateView):
	template_name = 'countries/home.html'
	#def get(self, request, *args, **kwargs):
	   # return render(request, "countries/home.html")

class CountryDetailView(TemplateView):
	template_name = 'countries/country_detail.html'

	def get_contex_data(self, *args, **kwargs):
		code = kwargs ['code']
		return {'code': code}

class CountryIdDetailView(DetailView):
	template_name = 'countries/country_id_detail.html'
	model = Country
		

class TagsView(TemplateView):
	template_name = 'countries/tags.html' 

class CountrySearchView(ListView):
    template_name = 'countries/search.html'
    model = Country

    def get_queryset(self):
        return Country.objects.filter(name__contains="e")