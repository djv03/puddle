from django.shortcuts import render

# Create your views here.
# all the routes are going to be here

def index(request):
    return render(request,'./core/index.html')