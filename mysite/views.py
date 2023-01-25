#this file is created by self
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello index page</h1>")


def about(request):
    return HttpResponse("About Page")
