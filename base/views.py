from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id':1,'name':'bharat','cast': 'thapa'},
    {'id':2,'name':'biwas','cast': 'stha'},
    {'id':3,'name':'chhabi','cast': 'acharya'},

]

def home(request):
    context = {'rooms':rooms}
    return render(request,"base/home.html",context)

def room(request,id):
    room = None
    for i in rooms:
        if i['id'] == int(id):
            room = i
    context = {'room':room}
    return render(request,"base/room.html",context)
