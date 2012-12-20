import simplejson as json
from django.shortcuts import render


def index(request):
    response = render(request, 'index.html')
    #response["P3P"] = 'CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"'
    response["P3P"] = 'CP="We do not have a P3P policy."'
    return response
