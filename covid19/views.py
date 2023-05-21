from django.shortcuts import render, redirect
import requests


# Create your views here.

def covid_view(request):
	return redirect('PL/')

def covid_view_cn(request, code):
	url = f'https://api.covid19api.com/summary'
	response = requests.get(url)
	data = response.json()
	return render(request, 'covid19/covid19.html', {'context' : data, 'code': code})