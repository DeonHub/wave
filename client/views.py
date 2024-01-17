from django.shortcuts import render
from superuser.models import *


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


def news_detail(request):
    template_name = 'client/news-detail.html'

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