import simplejson as json
from django.http import HttpResponse


def index(request):
    return HttpResponse('''
This page includes the third party javascript
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
<script src="http://thirdparty.com:8000/js?nocache=1"></script>
''')


def js(request):
    return HttpResponse(content_type='application/javascript', content='''
$(document).ready(function() {
    document.cookie = 'foo=bar';
    $.getJSON("http://thirdparty:8000/ajax?callback=?", null, function(data) {
        document.write('Cookie from server: ' + data.cookie);
    });
});
''')


def ajax(request):
    jsonp = '%(callback)s(%(data)s);' % dict(
        callback=request.GET.get('callback', ''),
        data=json.dumps({'cookie': request.COOKIES}))
    return HttpResponse(content_type='application/json', content=jsonp)
