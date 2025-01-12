from django.shortcuts import render, redirect
from .models import Profile, Post
from .forms import UserRegisterForm, PostForm, ProfileUpdateForm, UserUpdateForm


def home(request):
	posts = Post.objects.all()
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('home')
	else:
		form = PostForm()

	context = {'posts':posts, 'form' : form }
	return render(request, 'newsfeed.html', context)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = UserRegisterForm()

	context = {'form' : form}
	return render(request, 'register.html', context)

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return redirect('home') 

