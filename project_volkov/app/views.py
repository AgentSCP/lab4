from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def add(request):
    return render(request, "add.html")

def edit(request):
    return render(request, "edit.html")

def delete(request):
    return render(request, 'delete.html')