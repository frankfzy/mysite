from django.shortcuts import render
import json
from django.http import JsonResponse
from paltform.models import *
# Create your views here.


def addProject(request):
    data = json.loads(request.body.decode())
    print(data)
    name1 = data['name']
    description1 = data['description']
    add = Project(name=name1, description=description1)
    add.save()
    back = {
        'code': 200,
        'message': '添加成功'
    }
    # back = json.dumps(back)
    return JsonResponse(back)


def TwoProject(request):
    name2 = request.POST.get('name')
    description2 = request.POST.get('description')
    print(name2, description2)
    Project.objects.create(name=name2,description=description2)
    back = {
        'code': 200,
        'message': '添加成功'
    }
    # back = json.dumps(back)
    return JsonResponse(back)


def getProject(request):
    id = request.GET.get('id')
    print(id)
    # data = Project.objects.all().values()  # 查询库中所有有数据
    data = Project.objects.get(id=3).description
    print(data)
    # data = list(data)
    back = {
        'code': 200,
        'message': '查询成功',
        'data': data
    }
    return JsonResponse(back)







