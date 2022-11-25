from django.http import HttpResponse
from django.shortcuts import render

def Welcome(requent):
    return render(requent, 'index.html')

def User(request):
    username = request.GET['username']
    print(username)
    return render(request, 'user.html', {'name':username})