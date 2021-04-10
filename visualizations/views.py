from django.shortcuts import render


# returns the d3 visualization of the data.json file obtained from preprocessing directory
def index(request):
    return render(request, "visualizations/index.html")
