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
    data = Project.objects.get(id=2).description
    print(data)
    # data = list(data)
    back = {
        'code': 200,
        'message': '查询成功',
        'data': data
    }
    return JsonResponse(back)


def getProject2(request):
    # id = request.GET.get('id')
    # print(id)

    # data = Project.objects.all().values() # 查询库中所有有数据
    data = Project.objects.filter(name='火车票').values()
    print(data)
    data = list(data)
    back = {
        'code': 200,
        'message': '查询成功',
        'data': data
    }
    return JsonResponse(back)


def updataproject(request):
    data = json.loads(request.body.decode())
    name1 = data['name']
    description1 = data['description']
    id = data['id']
    Project.objects.filter(id=id).update(name=name1, description=description1)
    back = {
        'code': 200,
        'message': '修改成功',
        'data': data
    }
    return JsonResponse(back)


def deleteProject(request):
    # data = json.loads(request.body.decode())
    # id1 = data['id']
    # Project.objects.get(id=id1).delete()

    data = json.loads(request.body.decode())
    name = data['name']
    print(name)
    Project.objects.filter(name=name).delete()

    # id1 = data['id']
    # print(id1)
    # Project.objects.get(id=id1).delete()

    back = {
        'code': 200,
        'message': '删除成功',
    }
    return JsonResponse(back)


def addmodule(request):
    data = json.loads(request.body.decode())
    print(data)
    name1=data["name"]
    description1=data["description"]
    add = childMoudle(name=name1, description=description1)
    add.save()
    back = {
        'code': 200,
        'message': '添加成功'
    }
    # back=json.dumps(back)
    return JsonResponse(back)









