#from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def Movie_Name(request):
#     return HttpResponse("Hi There")


from django.shortcuts import render
# def Movie_Name(request):
#     return render(request,"base.html")

def Movie_Name(request):
    name = "waled ahmad"
    return render(request, "base.html", {"name": name})
def dd(request):
    name = "waled ahmad"
    return render(request, "about.html", {"name": name})
#def Movie_Name(request):


