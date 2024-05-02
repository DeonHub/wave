from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import requests
import datetime
import json
import random
import string
import os
import environ



# Create your views here.
@login_required(login_url='login:login')
def dashboard(request):
    template_name = 'superuser/dashboard.html'
    page = "Admin Dashboard"

    total_images = Image.objects.all().count()
    total_blogs = Blog.objects.all().count()

    return render(request, template_name, {
        'page': page,
        'total_blogs': total_blogs,
        'total_images': total_images
    })


@login_required(login_url='login:login')
def viewImages(request):
    template_name = 'superuser/view-images.html'
    page = "View Images"

    images = Image.objects.all()

    return render(request, template_name, {
        'page': page,
        'images': images
    }) 


@login_required(login_url='login:login')
def addImage(request):
    template_name = 'superuser/add-image.html'
    page = "Add Image"
    
    if request.method == 'POST':

        banner = True if request.POST.get('banner') else False
        image_name = request.POST.get('image_name')
        heading = request.POST.get('heading')
        subheading = request.POST.get('subheading')

        try:
            image_file = request.FILES.get('image_file')
        except:
            image_file = None 


        try:
            image = Image.objects.create(image_name=image_name, image_file=image_file, banner=banner, heading=heading, subheading=subheading)
            image.save()
            messages.success(request, 'Image added successfully')
            return HttpResponseRedirect(reverse('superuser:viewImages'))  
        except:
            messages.success(request, 'File size too large')
            return HttpResponseRedirect(reverse('superuser:addImage'))  


    else:
        return render(request, template_name, {
            'page': page,
        })


@login_required(login_url='login:login')
def editImage(request, id, **kwargs):
    template_name = 'superuser/edit-image.html'
    page = "Edit Image"

    image = Image.objects.get(id=id)
    
    if request.method == 'POST':
        new_image = request.FILES.get('image_file', None)
        if new_image is not None:
            
            image.image_file = request.FILES.get('image_file', None)

        image.image_name = request.POST.get('image_name')
        image.heading = request.POST.get('heading')
        image.subheading = request.POST.get('subheading')
        image.banner = True if request.POST.get('banner') else image.banner 

        try:
            image.save()

            messages.success(request, 'Image details updated successfully!')
            return redirect('superuser:viewImages')
        
        except:
            messages.success(request, 'File size too large')
            return HttpResponseRedirect(reverse('superuser:editImage', kwargs={'id': id}))

           
    
    else:
        return render(request, template_name, {
            'image': image,
            'page': page,
        }) 


@login_required(login_url='login:login')
def deleteImage(request, id, *args, **kwargs):
     
    if request.method == "POST":
        image = Image.objects.get(id=id)
        image.delete()

    messages.success(request, 'Image deleted successfully!')
    return redirect('superuser:viewImages')




@login_required(login_url='login:login')
def viewBlogs(request):
    template_name = 'superuser/view-blogs.html'
    page = "View Blogs"

    blogs = Blog.objects.all()

    return render(request, template_name, {
        'page': page,
        'blogs': blogs
    }) 


@login_required(login_url='login:login')
def addBlog(request):
    template_name = 'superuser/add-blog.html'
    page = "Add Blog"
    
    if request.method == 'POST':
        heading = request.POST.get('heading')
        subheading = request.POST.get('subheading')
        body = request.POST.get('body')

        try:
            blog_file = request.FILES.get('blog_file')
        except:
            blog_file = None 


        try:
            blog = Blog.objects.create(blog_file=blog_file, heading=heading, subheading=subheading, body=body)
            blog.save()
            messages.success(request, 'Blog added successfully')
            return HttpResponseRedirect(reverse('superuser:viewBlogs'))  
        except:
            messages.success(request, 'File size too large')
            return HttpResponseRedirect(reverse('superuser:viewBlogs'))  


    else:
        return render(request, template_name, {
            'page': page,
        })


@login_required(login_url='login:login')
def editBlog(request, id, **kwargs):
    template_name = 'superuser/edit-blog.html'
    page = "Edit Blog"

    blog = Blog.objects.get(id=id)
    
    if request.method == 'POST':
        new_image = request.FILES.get('blog_file', None)

        if new_image is not None:
            blog.blog_file = request.FILES.get('blog_file', None)

        blog.heading = request.POST.get('heading')
        blog.subheading = request.POST.get('subheading')
        blog.body = request.POST.get('body')

        try:
            blog.save()

            messages.success(request, 'Blog details updated successfully!')
            return redirect('superuser:viewBlogs')
        
        except:
            messages.success(request, 'File size too large')
            return HttpResponseRedirect(reverse('superuser:editBlog', id)) 

    else:
        return render(request, template_name, {
            'blog': blog,
            'page': page,
        }) 


@login_required(login_url='login:login')
def deleteBlog(request, id, *args, **kwargs):
     
    if request.method == "POST":
        blog = Blog.objects.get(id=id)
        blog.delete()

    messages.success(request, 'Blog deleted successfully!')
    return redirect('superuser:viewBlogs')


@login_required(login_url='login:login')
def viewBlog(request, id, *args, **kwargs):
    template_name = 'superuser/view-blog.html'
    page = "View Blog"

    blog = Blog.objects.get(id=id)

    return render(request, template_name, {
        'page': page,
        'blog': blog
    }) 




@login_required(login_url='login:login')
def viewVideos(request):
    template_name = 'superuser/view-videos.html'
    page = "View Videos"

    videos = Video.objects.all()

    return render(request, template_name, {
        'page': page,
        'videos': videos
    }) 


@login_required(login_url='login:login')
def addVideo(request):
    template_name = 'superuser/add-video.html'
    page = "Add Video"
    
    if request.method == 'POST':
        body = json.loads(request.body)
        banner = True if body['banner'] else False
        video_name = body['video_name']
        video_file = body['video_file']


        if video_file:
            video = Video.objects.create(video_name=video_name, video_file=video_file, banner=banner)
            video.save()
        else:
            pass    

        messages.success(request, 'Video added successfully')
        return HttpResponseRedirect(reverse('superuser:viewVideos'))      

    else:
        return render(request, template_name, {
            'page': page,
        })


@login_required(login_url='login:login')
def editVideo(request, id, **kwargs):
    template_name = 'superuser/edit-video.html'
    page = "Edit Video"

    video = Video.objects.get(id=id)

    if request.method == 'POST':
        body = json.loads(request.body)
        video.banner = True if body['banner'] else False
        video.video_name = body['video_name']
        video.video_file = body['video_file']
        video.save()

        messages.success(request, 'Video details updated successfully!')
        return redirect('superuser:viewVideos') 
    
    else:
        return render(request, template_name, {
            'video': video,
            'page': page,
            'id': id
        }) 


@login_required(login_url='login:login')
def deleteVideo(request, id, *args, **kwargs):
     
    if request.method == "POST":
        video = Video.objects.get(id=id)
        video.delete()

    messages.success(request, 'Video deleted successfully!')
    return redirect('superuser:viewVideos')




@login_required(login_url='login:login')
def profile(request):
    template_name = 'superuser/profile.html'
    page = "View Profile"

    return render(request, template_name, {
        'page': page
    }) 

@login_required(login_url='login:login')
def editProfile(request, id, **kwargs):
    template_name = 'superuser/edit-profile.html'
    page = "Edit Profile"

    return render(request, template_name, {
        'page': page
    }) 





@login_required(login_url='login:login')
def resetPassword(request):
    template_name = 'superuser/reset-password.html'
    page = 'Reset Password'
    user=request.user


    if request.method == 'POST':
        password = request.POST.get('password')

        password = make_password(password)
        admin = User.objects.get(id=user.id)

        admin.password = password
        admin.save()

        messages.success(request, 'Password reset successfully!')
        return redirect('superuser:dashboard')

    else:
        return render(request, template_name, {
            'page': page
        })



def user_logout(request):
    logout(request)
    return redirect('login:login')   


   