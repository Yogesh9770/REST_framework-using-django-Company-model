from django.http import HttpResponse, JsonResponse

def Home_page(request):
    print("Home page is requested")
    friends ={
        "name":"John",
        "age":30,
        "city":"New York"
    }
    return JsonResponse(friends,)