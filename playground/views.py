from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        # "name": "D-Coders"
    }
    return render(request, 'index.html', context=context)