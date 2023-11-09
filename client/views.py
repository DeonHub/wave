from django.shortcuts import render

# Create your views here.
def index(request):
    template_name = 'client/index.html'

    return render(request, template_name, {

    })


def index_top_menu(request):
    template_name = 'client/index-top-menu.html'

    return render(request, template_name, {
        
    })


def index_video(request):
    template_name = 'client/index-video.html'

    return render(request, template_name, {
        
    })

def showcase(request):
    template_name = 'client/showcase.html'

    return render(request, template_name, {
        
    })


def wave(request):
    template_name = 'client/wave.html'

    return render(request, template_name, {
        
    })


def services(request):
    template_name = 'client/services.html'

    return render(request, template_name, {
        
    })


def news(request):
    template_name = 'client/news.html'

    return render(request, template_name, {
        
    })


def news_detail(request):
    template_name = 'client/news-detail.html'

    return render(request, template_name, {
        
    })


def work_detail(request):
    template_name = 'client/work-detail.html'

    return render(request, template_name, {
        
    })


def contact(request):
    template_name = 'client/contact.html'

    return render(request, template_name, {
        
    })  


def career(request):
    template_name = 'client/career.html'

    return render(request, template_name, {
        
    }) 

def documentation(request):
    template_name = 'client/documentation.html'

    return render(request, template_name, {
        
    })      