from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .models import RequestDataJson, RequestDataText

@csrf_exempt
@require_POST
def call(request): 
    data = request.body
    try :
        data = data.decode('utf-8')
    except:
        pass

    if request.headers.get('content-type')  =='application/json':
        with open('output.json','a',encoding='utf-8') as fj:
            fj.write(data+'\n\n')
            data = json.loads(data)
            RequestDataJson.objects.create(data = data)
    else:
        with open('output.txt','a',encoding='utf-8') as f:
            f.write(data+'\n\n')
            RequestDataText.objects.create(data = data)


    print(data) 
    return HttpResponse("success",status=200)

# Create your views here.
