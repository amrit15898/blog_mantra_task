from django.shortcuts import render, redirect
from django.contrib.auth.models import *
from django.db.models import Q
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .helper import send_mail_to_user
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def sign_up(requset):
    if requset.method == "POST":
        try:
            first_name = requset.POST.get("fname")
            last_name = requset.POST.get("last_name")
            username = requset.POST.get("username")
            email = requset.POST.get("email")
            password = requset.POST.get("password")
            # Check if email already exists
            check_email = User.objects.filter(email=email).first()
            if check_email:
                messages.error(requset, "Email already exists")
                return redirect("sign-up")
            
            user_obj = User.objects.filter(username = username).first()
            if user_obj:
                messages.error(requset, "Try with different username this username alread exists")
                redirect("sign-up")

            # Create the user object
            obj = User(first_name=first_name, last_name=last_name, username=username, email=email)
            obj.set_password(password)
            obj.save()
            messages.success(requset, "Signup successful")
            return redirect("/")
        
        except Exception as e:
            messages.error(requset, f"An error occurred: {e}")
            return redirect("/sign-up")
        
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
    try:
        blogs = BlogPost.objects.all()
        itmes_per_page = 3
        paginator  = Paginator(blogs, itmes_per_page)  
        page_no = request.GET.get("page")
        page_obj = paginator.get_page(page_no)
        context = {"blogs": page_obj} 
    except Exception as e:
        messages.error(f"An error occured {e}")
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
        elif request.user.is_authenticated:
            comment = request.POST.get("cmnt")
            obj = Comment(Blog=blog, author=request.user, content=comment)
            obj.save()
        else:
            messages.error(request, "Please log in to post a comment.")
    
    context["blog"] = blog
    return render(request, "detail-blog.html" , context)


def like_comment(request, id):
    try:
        comment = Comment.objects.get(id=id)

    except Comment.DoesNotExist:
        pass

    user = request.user
    if request.user.is_authenticated:
        # Check if the user has already liked this comment
        already_liked = comment.like.filter(id=user.id).exists()

        if already_liked:
            comment.like.remove(user)
            messages.success(request, "Comment unliked successfully.")
        else:
            comment.like.add(user)
            messages.success(request, "Comment liked successfully.")
    else:
        messages.error(request, "Please log in before liking a comment.")
    return redirect(request.META.get('HTTP_REFERER', '/'))


def logout_page(request):
    print("This functio calling")
    logout(request)
    return redirect("/")