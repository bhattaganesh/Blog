from  django.shortcuts import HttpResponse,render
from  blog.models import Post

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
        'posts' : Post.objects.all()
        }
    return render(request,'home.html',context)
    