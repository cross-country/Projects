from django.http import HttpResponse

def index(request):
    return HttpResponse("Here you will see a list of advertisments")
