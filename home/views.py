from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .helper import send_mail_to_user
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def sign_up(requset):
    if requset.method == "POST":
        first_name = requset.POST.get("fname")
        last_name = requset.POST.get("lname")
        username = requset.POST.get("username")
        email = requset.POST.get("email")
        password = requset.POST.get("password")

        check_email = User.objects.filter(email=email).first()
        if check_email:
            messages.error(requset, "Email alread exists")
            return redirect("sign-up")

        obj = User(first_name = first_name, last_name=last_name, username=username, email=email)
        obj.set_password(password)
        obj.save()
        messages.success(requset, "Signup successfullly")
        return redirect("/")
        
    return render(requset, "sign-up.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        check_user = User.objects.filter(username = username).first()
        if not check_user:
            messages.warning(request, "User does not exit")
            return redirect("login/")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("/")
            
        else:
            messages.error("Invalid login credentails")
            return redirect("login/")


    return render(request, "login.html")

def home_page(request):
    blogs = BlogPost.objects.all()
    print(blogs)
    context = {"blogs": blogs} 
    return render(request, "home.html", context)

def detail_blog(request, id):
    try:
        blog = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        return messages.error(request, "blog does not exit")
    comments = blog.all_comments.all()
    blog_detail_url = request.build_absolute_uri(reverse('detailblog', args=[blog.id]))
    print(blog_detail_url)
    context = {}
    context["comments"] = comments
    if request.method == "POST":

        if "send_email" in request.POST:
            recipient_email = request.POST.get("recipient-email")
            send_mail_to_user("Desi Coders", blog_detail_url, "none76845@gmail.com", recipient_email)

        else:
            comment = request.POST.get("cmnt")
            print(f"this is my comment {comment}")
            obj = Comment(Blog = blog , author = request.user, content = comment)
            obj.save()
    
    context["blog"] = blog
    return render(request, "detail-blog.html" , context)


def like_comment(request, id):
    try:
        comment = Comment.objects.get(id=id)

    except Comment.DoesNotExist:
        print("comment does not exits")

    user = request.user
    check_comment_exist =  Comment.objects.filter(like=user, Blog = comment.Blog)
    if check_comment_exist:
        comment.like.remove(request.user)

    else:
        comment.like.add(request.user)

    return redirect(request.META.get('HTTP_REFERER', '/'))


