import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from youtube_comments import getCommentsFiltered
from review import getVideoStatistics


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
        
        youtube_video_url = "https://www.youtube.com/watch?v=n9XX_zz3bi8"

        comments = getCommentsFiltered(youtube_video_url, 10, True)
        positive_comments_count = len(comments["positive_comments"])
        negative_comments_count = len(comments["negative_comments"])

        video_statistics = getVideoStatistics(youtube_video_url)

        data = {
            "comments": comments,
            "isVideoGood": (video_statistics["likes"] >= video_statistics["views"] / 1000) and positive_comments_count > negative_comments_count,
            "message": "Successful"
        }

        print(json.dumps(data, indent=2))
        my_object = {
            "name": name,
            "age": 30,
            "email": "johndoe@example.com"
        }
        return JsonResponse(data)
    else:
        # Return a 405 Method Not Allowed error for other request methods
        return HttpResponseNotAllowed(['GET'])


