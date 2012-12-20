import simplejson as json
from django.http import HttpResponse


def index(request):
    return HttpResponse('''
This page includes the third party javascript
<script type="text/javascript">var NREUMQ=NREUMQ||[];NREUMQ.push(["mark","firstbyte",new Date().getTime()]);</script>
<script type="text/javascript">if(!NREUMQ.f){NREUMQ.f=function(){NREUMQ.push(["load",new Date().getTime()]);
var e=document.createElement("script");e.type="text/javascript";e.src=(("http:"===document.location.protocol)?"http:":"https:")+"//"+"d1ros97qkrwjf5.cloudfront.net/42/eum/rum.js";
document.body.appendChild(e);if(NREUMQ.a)NREUMQ.a();};NREUMQ.a=window.onload;window.onload=NREUMQ.f;};
NREUMQ.push(["nrfj","thirdparty.com:8000","2d8ca8bf04","885531","b1NbN0EFWBcEURFRDlYZfxZdB0INClxKXgBWW14OR0paBQtWDFYGFkBQBkQXDAAEQQ1aDllEXQ==",0,821,new Date().getTime(),"","","","",""]);</script>
''')


def ajax(request):
    print request.COOKIES
    return HttpResponse('done')
