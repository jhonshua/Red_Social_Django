from django.shortcuts import render
from .models import Profile, Post


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    print(context)
    return render ( request, 'newsfeed.html', context)