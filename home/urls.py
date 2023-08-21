from django.urls import path, include
from .views import *

urlpatterns = [

    path("", home_page, name="home"),
    path("sign-up", sign_up , name="signup"),
    path("detail-blog/<id>", detail_blog, name="detailblog"),
    path("like-comment/<id>", like_comment, name="like_comment"),
    path("login/", login_page, name="login"),
    path("logout", logout_page, name="logout")
]
