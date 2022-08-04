from django.http import HttpResponse, JsonResponse
import requests
import simplejson as json
import jwt
from time import time


def create_meet(request):
    dict = json.loads(request.body)
    try:
        header = {
            "authorization" : "Bearer {}".format(dict["token"])
        }
    except:
        return HttpResponse("You also need to enter the access token")
    data = requests.post("https://api.zoom.us/v2/users/me/meetings", headers = header, json = dict)
    if data.status_code == 201:
        data = data.json()
        return JsonResponse({"Host Join Link" : data["start_url"], "Participant's Join Link" : data["join_url"]})
    
    return HttpResponse(data)


def authorize(request):
    dict = json.loads(request.body)
    token = jwt.encode({"iss" : dict["API_KEY"], "exp" : time() + 7200}, dict["API_SEC"], algorithm="HS256")
    return JsonResponse({"Your Token " : token, "Expires in" : "2 hours"})
