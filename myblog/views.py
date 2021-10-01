from  django.shortcuts import HttpResponse,render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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

@login_required(login_url='signin')

def dashboard(request):
    return render(request,'dashboard.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(username = username, password = pwd)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.add_message(request,messages.ERROR,"Username or passsword does not match")
            return redirect("signin")
    return render(request,'login.html')


def signup(request):
    context = {}
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        context.update({
            "firstname" : fname,
            "lastname" : lname,
            "username" : username,
            "email" : email
        })
        if len(username) == 0:
            messages.add_message(request,messages.ERROR,"Sorry!, username can't be empty")
            return render(request,'signup.html',context)

        if pwd == cpwd:
            user = User(username = username, first_name = fname, last_name = lname, email = email)
            user.set_password(pwd)
            try:
                user.save()
                messages.add_message(request,messages.SUCCESS,"Signup Successful")
                return redirect("signin")
            except Exception as e:
                messages.add_message(request,messages.ERROR,e)
                return render(request,'signup.html',context)
        else:
            messages.add_message(request,messages.ERROR,"Sorry!, confirmation password does not match")
            return render(request,'signup.html',context)
    return render(request,'signup.html',context)

def signout(request):
    logout(request)
    return redirect('signin')
