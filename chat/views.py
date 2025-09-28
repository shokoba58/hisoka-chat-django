from django.shortcuts import render

def index(request):
    return render(request, "chat/index.html")

def room(request, slug):
    return render(request, "chat/room.html", {"room_name": slug})