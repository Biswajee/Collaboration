from django.shortcuts import render

def index(request):
    return render('visualizations/index.html')
