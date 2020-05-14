from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages 
from .forms import NewUserForm, PostForm
from .models import Post


def single_slug(request, single_slug):
	categories=[c.category_slug for c in TutorialCategory.objects.all()]
	if single_slug in categories:
		matching_series=TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
			
		series_urls={}
		for m in matching_series.all():
			part_one=Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
			series_urls[m]=part_one.tutorial_slug


		return render(request,
				      "main/category.html",
				      {"part_ones":series_urls})

	tutorials=[t.tutorial_slug for t in Tutorial.objects.all()]
	if single_slug in tutorials:
		this_tutorial=Tutorial.objects.get(tutorial_slug=single_slug)
		tutorial_from_series=Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by("tutorial_published")
		this_tutorial_idx=list(tutorial_from_series).index(this_tutorial)
		

		return render(request,
					  "main/tutorial.html",
					  {"tutorial":this_tutorial,
					   "sidebar": tutorial_from_series,
					   "this_tutorial_idx":this_tutorial_idx})
					   
		
		return HttpResponse(f"{single_slug} is a tutorial!!!")
	return HttpResponse(f"{single_slug} does not correspond to anything.")


# Create your views here.
def homepage(request):
	return render(request=request,
				  template_name="main/categories.html",
				  context={"categories": TutorialCategory.objects.all})
	#HttpResponse("Wow this is an <strong>awesome</strong> tutorial") 

def register(request):
	if request.method=="POST":
		form=NewUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}: {form.error_messages[msg]}")

	form= NewUserForm
	return render(request,
				  "main/register.html",
				  context={"form": form})

def logout_request(request):
	logout(request)
	messages.info(request,"logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method=="POST":
		form=AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password")
	else:
		messages.error(request,"Invalid username or password")


	form=AuthenticationForm()
	return render(request,
				  "main/login.html",
				  {"form":form})

def get_workstamp(request):
	form=PostForm(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			instance=form.save(commit=False)
			title=form.cleaned_data.get('title')
			image=form.cleaned_data.get('cover')
			timestamp=form.cleaned_data.get('timestamp')
			instance.save()
			messages.success(request, f"ทำการลงชื่อเข้าทำงานสำเร็จ: {title}, เมื่อเวลา: {timestamp}")
			return redirect("main:homepage")
		
	context={
	"form":form,
	}

	return render(request,"main/post_form.html",context)

def post_detail(request):
	#instance=Post.objects.get(id=3)
	context= {
			"title":"Detail"
	}
	return render(request, "main/index.html",context)

def post_list(request):
	queryset = Post.objects.all()
	context={
		"object_list": queryset,
		"title":"List"
	}
	return render(request, "main/index.html", context)

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")


class CreatePostView(CreateView):
	model=Post
	form_class= PostForm
	template_name='main/post.html'
	success_url=reverse_lazy('main:homepage')

