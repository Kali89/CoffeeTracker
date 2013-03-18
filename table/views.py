from django.http import HttpResponse

from table.models import Scores

def index(request):
    latest_scores = Scores.objects.all()
    output = ', '.join([p.buyer for p in latest_scores])
    return HttpResponse(output)


def table(request):
    return HttpResponse("You're looking at the table page.")
