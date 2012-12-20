from django.shortcuts import render


def p3p(response):
    response["P3P"] = 'CP="We do not have a P3P policy."'
    return response


def index(request):
    return p3p(render(request, 'index.html'))


def rum(request):
    return p3p(render(request, 'rum.js'))


def beacon(request):
    print 'COOKIE: %s' % request.COOKIES
    return p3p(render(request, 'beacon.html'))
