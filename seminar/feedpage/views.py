from django.shortcuts import render, redirect
from .models import Feed

def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.create(title=title, content=content)
        return redirect('/feeds')

def new(request):
    return render(request, 'feedpage/new.html')


def show(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/show.html', {'feed': feed})

def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds')
