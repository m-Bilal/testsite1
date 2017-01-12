from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from process.models import User
# Create your views here.

def hello(request):
    return HttpResponse("Process App Working")


@csrf_exempt
def add_user(request):
    post_first_name = request.POST.get("first_name", "")
    post_last_name = request.POST.get("last_name", "")
    post_message = request.POST.get("message", "")

    user = User(first_name = post_first_name, last_name = post_last_name, message = post_message)
    user.save()
    return HttpResponse('User: %s %s saved' % (post_first_name, post_last_name))


@csrf_exempt
def delete_all_users(request):
    User.objects.all().delete()
    return HttpResponse("All users deleted")


@csrf_exempt
def get_all_users(request):
    u = User.objects.all()
    user_json = []
    for i in u:
        user_json = [{
            'first_name' : i.first_name,
            'last_name' : i.last_name,
            'message' : i.message
        }]
    json_response = {'user' : user_json}
    return JsonResponse(json_response)