from django.shortcuts import render, redirect
from .models import Post, Comment
import pdb

# Create your views here.
def newsfeed(request):
    if request.method == "POST":
        name = request.POST.get('name')
    posts = Post.objects.all().order_by('-id')
    if 'name' in request.session:
        name = request.session['name']
    return render(request, 'pages/newsfeed.html', {'name': name, 'posts': posts})


def write(request):
    if request.method == "POST":
        name = request.POST.get('name')
    
    return render(request, 'pages/write.html', {'name': name})


def success(request):
    if request.method == "POST":
        global name
        name = request.POST.get('name')
        content = request.POST.get('content')
        image = request.FILES.get('file')
        
        post = Post(name=name, content=content, img=image)
        post.save()
        return redirect('success')
        
    return render(request, 'pages/success.html', {'name': name})
    
    
def create_comment(request):
    if request.method == "POST":
        writer = request.POST.get('writer')
        message = request.POST.get('message')
        post_id = request.POST.get('post')
        post = Post.objects.get(pk=post_id)
        comment = Comment(writer=writer, message=message, post=post)
        comment.save()
        request.session['name'] = writer
        return redirect('newsfeed')