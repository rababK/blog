from django.shortcuts import render
from .models import post
from .forms import PostForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
def home(request):
    POSTS=post.objects.all()[:]
    context={
        "posts":POSTS
    }
    return HttpResponse(render(request,"home.html",{"POSTS":POSTS}))
def CreatePost(request):
    if request.method == 'POST':
        postform=PostForm(request.POST)
        if postform.is_valid():
            postform.save()
            return HttpResponseRedirect(reverse("blog:home"))
        else:
            ErrorMessage=" some information are missed "
            context = {
                "ErrorMessage":ErrorMessage,
                "postform":postform
            }
            return render (request, "home.html", context=context)
    else:
        postform = PostForm ()
        context = {

            "postform": postform
        }

        return render (request, "post.html", context=context)
def PostDetails(request,pk):
    Post=post.objects.get(pk=pk)
    context = {

        "post": Post
    }

    return render (request, "content.html", context=context)

