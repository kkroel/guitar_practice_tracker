from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return render(request, 'Welcome to guitar_site')
    return HttpResponse('Welcome to guitar_site')
