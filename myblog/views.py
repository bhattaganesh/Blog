from  django.shortcuts import HttpResponse,render, get_object_or_404,redirect
from  blog.models import Post
from blog.form import BlogForm
def about(request):
    # return HttpResponse("About Page")
    context = {
        'title' : "About Us Page"
    }
    return render(request,'about.html',context)
def contact(request):
    # return HttpResponse("<h1>Contact Page</h1>")
    context = {
        'title' : "Contact Us Page"
    }
    return render(request,'contact.html',context)

def home(request):
    context = {
        'posts' : Post.objects.all()[::-1]
        }
    return render(request,'home.html',context)

def detail(request, id):
    # post = Post.objects.get(pk = id)
    post = get_object_or_404(Post, id = id)
    context = {
        'post' : post
    }
    return render(request,'detail.html',context)

def deleteBlog(request, id):
    post = get_object_or_404(Post, pk = id)
    post.delete()
    return redirect('home')

def createBlog(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form' : form
    }
    return render(request,'create-blog.html',context)

def updateBlog(request,id):
    post = get_object_or_404(Post,id=id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form' : form
    }

    return render(request,'update-blog.html',context)