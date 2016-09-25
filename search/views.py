from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import KeyWords, Topics

def topics(request):
    topics = Topics.objects.all()
    context = {"topics": topics}
    return render(request, 'search/search.html', context)

def keywords(request):
    keywords = KeyWords.objects.all()
    context = {"keywords": keywords}
    return render(request, 'search/search.html', context)


