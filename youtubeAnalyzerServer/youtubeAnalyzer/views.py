import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def home(request):
    return HttpResponse('Home')

def postRequest(request):
    if request.method == 'POST':
        # Do something with the POST data
        data = json.loads(request.body)
        url = data.get('url')
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def GetRequest(request, name):
    if request.method == 'GET':
        my_object = {
            "name": name,
            "age": 30,
            "email": "johndoe@example.com"
        }
        return JsonResponse(my_object)
    else:
        # Return a 405 Method Not Allowed error for other request methods
        return HttpResponseNotAllowed(['GET'])


