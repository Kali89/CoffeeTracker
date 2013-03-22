from django.http import HttpResponse

from table.models import Scores

def index(request):
    return HttpResponse("This be the homepage.")


def table(request):
    return HttpResponse("You're looking at the table page.")
