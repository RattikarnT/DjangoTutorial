"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import CreatePostView

app_name = "main"

urlpatterns = [
  path("", views.homepage, name="homepage"),  
  path("post",CreatePostView.as_view(),name="add_post"),
  path("workstamp",views.get_workstamp, name="work_stamp"),
  path("detail",views.post_detail, name="post_detail"),
  path("list",views.post_list, name="post_list"),
  path("update",views.post_update, name="post_update"),
  path("delete",views.post_delete, name="post_delete"),
  path("register/", views.register, name="register"),
  path("logout/",views.logout_request, name="logout"),
  path("login/",views.login_request, name="login"),
  path("<single_slug>", views.single_slug, name="single_slug"),
]    

#urlpatterns += staticfiles_urlpatterns()
#if settings.DEBUG:
urlpatterns += staticfiles_urlpatterns()
  #urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
