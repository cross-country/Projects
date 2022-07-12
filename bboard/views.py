from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from .models import Bb

"""
def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
"""

def index(request):
    #bbs = Bb.objects.order_by('-published')
    #I changed the previous string, cos we do not need sorting
    bbs = Bb.objects_all()
    return render(request, 'bboard/index.html', {'bbs': bbs})

