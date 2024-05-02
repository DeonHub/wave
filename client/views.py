from django.shortcuts import render
from superuser.models import *
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import environ
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect, render

env = environ.Env()
environ.Env.read_env()


# Create your views here.
def index(request):
    template_name = 'client/index.html'
    images = Image.objects.all()
    videos = Video.objects.all()
    banners = Image.objects.filter(banner=True)

    if videos.count() > 0:
        video = videos.first()
    else:
        video = None  



    return render(request, template_name, {
        'images': images,
        'videos': videos,
        'banners': banners,
        'video': video
    })

    

def index_top_menu(request):
    template_name = 'client/index-top-menu.html'

    images = Image.objects.all()
    videos = Video.objects.all()
    banners = Image.objects.filter(banner=True)

    if videos.count() > 0:
        video = videos.first()
    else:
        video = None  

    return render(request, template_name, {
        'images': images,
        'videos': videos,
        'banners': banners,
        'video': video
    })


def index_video(request):
    template_name = 'client/index-video.html'

    images = Image.objects.all()
    videos = Video.objects.all()
    banners = Image.objects.filter(banner=True)

    if videos.count() > 0:
        video = videos.first()
    else:
        video = None  

    return render(request, template_name, {
        'images': images,
        'videos': videos,
        'banners': banners,
        'video': video
    })


def showcase(request):
    template_name = 'client/showcase.html'

    images = Image.objects.all()
    videos = Video.objects.all()
    banners = Image.objects.filter(banner=True)

    if videos.count() > 0:
        video = videos.first()
    else:
        video = None  

    return render(request, template_name, {
        'images': images,
        'videos': videos,
        'banners': banners,
        'video': video
    })


def wave(request):
    template_name = 'client/wave.html'

    images = Image.objects.all()
    videos = Video.objects.all()
    banners = Image.objects.filter(banner=True)

    if videos.count() > 0:
        video = videos.first()
    else:
        video = None    


    return render(request, template_name, {
        'images': images,
        'videos': videos,
        'banners': banners,
        'video': video
    })


def services(request):
    template_name = 'client/services.html'

    images = Image.objects.all()
    videos = Video.objects.all()
    banners = Image.objects.filter(banner=True)

    if videos.count() > 0:
        video = videos.first()
    else:
        video = None  

    return render(request, template_name, {
        'images': images,
        'videos': videos,
        'banners': banners,
        'video': video
    })


def news(request):
    template_name = 'client/news.html'

    blogs = Blog.objects.all()

    return render(request, template_name, {
        'blogs': blogs
    })



def news_detail(request, id, *args, **kwargs):
    template_name = 'client/news-detail.html'
    page = "View Blog"

    blog = Blog.objects.get(id=id)

    return render(request, template_name, {
        'page': page,
        'blog': blog
    }) 



def work_detail(request):
    template_name = 'client/work-detail.html'

    images = Image.objects.all()
    videos = Video.objects.all()
    banners = Image.objects.filter(banner=True)

    if videos.count() > 0:
        video = videos.first()
    else:
        video = None  

    return render(request, template_name, {
        'images': images,
        'videos': videos,
        'banners': banners,
        'video': video
    })


def contact(request):
    template_name = 'client/contact.html'

    if request.method == 'POST':

        user_name = request.POST.get('name')
        user_email = request.POST.get('email')
        user_subject = request.POST.get('subject')
        user_message = request.POST.get('message')

        # Function to send mail to admin
        subject = f'NEW CONTACT FORM ENTRY'
        body = f"""
                    A user contacted you through the contact form on your website.
                    Find the details below:
                    Name: { user_name }
                    Email: { user_email} 
                    Subject: { user_subject }
                    Message: { user_message }

                """
        senders_mail = settings.EMAIL_HOST_USER
        to_address = ['admin@nickelwaves.com']

        email = EmailMessage(subject, body, senders_mail, to_address)

        try:
            email.send()
            # pass
        except: 
            print("Server error")
            pass

        messages.success(request, 'Contact details submitted successfully. We will get back to you shortly.')
        return HttpResponseRedirect(reverse('client:contact'))          

    else:
        return render(request, template_name, {

        })



def career(request):
    template_name = 'client/career.html'

    images = Image.objects.all()
    videos = Video.objects.all()
    banners = Image.objects.filter(banner=True)

    if videos.count() > 0:
        video = videos.first()
    else:
        video = None  

    return render(request, template_name, {
        'images': images,
        'videos': videos,
        'banners': banners,
        'video': video
    })



def documentation(request):
    template_name = 'client/documentation.html'

    return render(request, template_name, {
        
    })      