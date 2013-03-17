from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi - you're at the table index.")
