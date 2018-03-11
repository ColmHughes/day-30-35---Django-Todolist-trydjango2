from django.shortcuts import render

# Create your views here.
def add_comment(request):
    return render(request, "comments/index.html")