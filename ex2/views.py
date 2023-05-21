import random
import requests
from django.shortcuts import render

# Create your views here.
def home_views(request):
	return render(request, 'ex2/index.html',)

def contact_views(request):
	return render(request, 'ex2/contact.html', )

def about_view(request):
	lucky_number = random.randint(1, 10)
	unlucky_number =  random.randint(1, 10)
	mytech = [{'name': 'HTML','url': 'https://www.w3schools.com/html/','level': 'beginner'},
	   {'name': 'CSS','url': 'https://www.w3schools.com/css/','level': 'beginner'},
       {'name': 'Bootstrap','url': 'https://getbootstrap.com','level': 'beginner'},
       {'name': 'Python','url': 'https://www.python.org','level': 'intermediate'},
       {'name': 'Django','url': 'https://www.djangoproject.com','level': 'beginner'      },    ]
	
	nums = {'lucky_number':lucky_number, 'unlucky_number':unlucky_number, 'lang':mytech}
	
	return render(request, 'ex2/about.html', nums)

def news_view(request):
	API_KEY = '77d75d95172b47a2bb99e76c2c9de91c'
	source = 'new-scientist'
	url = f'https://newsapi.org/v2/everything?sources={source}&apiKey={API_KEY}'
	response = requests.get(url)
	data = response.json()
	context = {'newsapi': data}
	return render(request, 'ex2/news.html', context)


