from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# Create your views here.

def test(request):
    return render(
        request,
        'meow/main.html'
    )
