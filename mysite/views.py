from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def rum(request):
    return render(request, 'rum.js')


def beacon(request):
    print 'COOKIE: %s' % request.COOKIES
    response = render(request, 'beacon.html')
    response.set_cookie('JSESSIONID', '9171121a5dc576e2')
    #response["P3P"] = 'CP="We do not have a P3P policy."'
    return response
