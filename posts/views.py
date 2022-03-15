from django.shortcuts import render
from django.http.response import HttpResponseBase,HttpResponseRedirect

from django import forms
from .models import Post
from .forms import PostForm
from django.http import HttpResponse

def index(request):
    #If the method is post
    if request.method == 'POST':
       form = PostForm(request.POST, request.FILES)
       # If the form is valid
       if form.is_valid():
           #Yes, Save
           form.save()
           
           # Redirect to Home
           return HttpResponseRedirect('/')
       
       else:
            #No, Show Error
            return HttpResponseRedirect(form.errors.as_json())
    #Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
         
    #Show
    return render(request,'posts.html',
                       {'posts': posts})
    
def delete(request, post_id):
        # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
    newlikecount= Post.objects.get(id=post_id)
    newlikecount.likecount +=1
    newlikecount.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    posts= Post.objects.get(id=post_id)
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, 'edit.html',{'posts':posts})
        

                   
          
         
         
         
         
        
    
 
                  
    
     
