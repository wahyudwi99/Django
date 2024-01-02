from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Halo anda sedang di halaman home !!")

def login(request):
    return render(request, 'template_login.html')

@csrf_exempt
def login_output(request):
    # get value from html
    username = request.POST['username']
    print(username)
    return render(request, 'result.html')

@api_view(['POST'])
def test_aja(request):
    isi = 'transformer'
    return Response(isi)
    # return Response()