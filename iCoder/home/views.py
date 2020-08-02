from django.shortcuts import render, HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(requests):
    # return HttpResponse("we are at home page of our project")
    return render(requests, 'home/home.html')


def about(requests):
    return render(requests, 'home/about.html')


def contact(request):
    # messages.success(request, 'Profile details updated.')
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        
        if  len(name) < 2 or len(email) < 4 or len(phone) < 9 or len(content) < 10:
            messages.error(request, 'Please provide proper credentials')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'Your form has been successfully submitted')
        # print('we are using post request')
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    allPosts = Post.objects.filter(title__icontains = query)
    context = {'allPosts': allPosts}

    return render(request, 'home/search.html',context)
    # return HttpResponse('This is search')

def handleSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass2']
        pass2 = request.POST['pass2']
        print(fname,lname)


        myuser= User.objects.create_user(username,email,pass1)
        myuser.First_name = fname
        myuser.Last_name = lname
        myuser.Phone = phone
        myuser.save()
        messages.success(request,"Your account has been created successfully")
        return redirect ('home')


    else:
        return HttpResponse('404 - Not found')


def handlelogin(request):
    if request.method == 'POST':
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']

        user = authenticate(username=loginUsername, password=loginPassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'Please provide correct credentials')
            return redirect('home')
    else:
        return HttpResponse('404 - Not found')


def handlelogout(request):
    logout(request)
    messages.success(request, 'You are successfully logged out')
    return redirect('home')
    
