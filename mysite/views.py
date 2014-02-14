from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogapp.models import blog_database #database access
from django.views.decorators.csrf import csrf_exempt #for security checking


def welcome(request):
    return render(request, 'home.html') #load html file


def home(request):
	posts=[dict(id=i.id, author=i.author, post=i.post) for i in blog_database.objects.order_by('id')]
	if request.session['logged_in']:
		 return render(request, 'home_logout.html', {'posts': posts})
	else:
		return render(request, 'home.html', {'posts': posts})

@csrf_exempt
def post(request):
	if request.method == 'GET':
		if request.session['logged_in']:
    			return render(request, 'post.html')
		else:
			return redirect('mysite.views.login')
	else:
		author=request.POST.get('name')
    		post=request.POST.get('blogpost')
    		insert=blog_database(author=author, post=post)
    		insert.save()
    		return render(request, 'post.html')
@csrf_exempt
def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	else:
		if request.POST.get('username') == "sanal" and request.POST.get('password') == "tharayil":
			request.session['logged_in']= True
			return  redirect('mysite.views.post')
		else:
			error="username and password didnt match"
			return render(request, 'login.html', {'error' : error})
			
def logout(request):
	request.session['logged_in'] = False
	return redirect('mysite.views.login')
