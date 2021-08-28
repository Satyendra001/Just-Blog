from django.shortcuts import redirect, render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})


def post(request,pk):
    if pk == 'index':
        return render(request,'index.html')
    post = Post.objects.get(id = pk)
    return render(request, 'post.html', {'post':post})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def newpost(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['title']
        body = request.POST['body']

        addPost = Post.objects.create(name = name, title=title, body=body)
        addPost.save()
        return redirect('index')
    
    else:
        return render(request,'newpost.html')
    
