from django.shortcuts import render
<<<<<<< HEAD
from django.utils import timezone
from .models import Post

# Create your views here.

def articles_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'articles_list.html', {'posts':posts}) 
=======

# Create your views here.

def article_list(request):
	return render(request, 'article_list.html');
	
>>>>>>> 7e88efda4da329363e4b3c4565a61ee381ba6e4d
