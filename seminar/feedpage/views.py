from django.shortcuts import render, redirect
from .models import Feed


def index(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()
        return render(request, 'feedpage/index.html', {'feeds': feeds})

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        feed = Feed.objects.create(title=title, content=content)
        return redirect('/feeds/%d/' %feed.id)


def new(request):
    return render(request, 'feedpage/new.html')


def show(request, id):
    if (request.method == 'GET'):
        feed = Feed.objects.get(id=id)
        return render(request, 'feedpage/show.html', {'feed': feed})
    
    elif (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        Feed.objects.update(id=id, title=title, content=content)
        return redirect('/feeds/%d/' %id)


def edit(request, id):
    feed = Feed.objects.get(id=id)
    return render(request, 'feedpage/edit.html', {'feed': feed})


def delete(request, id):
    feed = Feed.objects.get(id=id)
    feed.delete()
    return redirect('/feeds/')
