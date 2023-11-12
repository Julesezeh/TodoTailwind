from django.shortcuts import render
from .models import Todo

# Create your views here.
def index(request):
    results = Todo.objects.filter(user=request.user)
    print("results",results)
    return render(request,"home.html",{"todos":results})