from django.shortcuts import render
from django.http import HttpResponse
from sqlapp.models import Fruit

# Create your views here.
num1=0

def xgdelete(request):
    return render(request,'xgrevise.html')
def selectlist(request):
    return render(request, 'syquest.html')
def zjnature(request):
    return render(request,'zjnature.html')
def cxquest(request):
    return render(request, 'cxquests.html')
def scdelete(request):
    return render(request, 'scdelete.html')
def selsect(request):#添加数据
    stuid=int(request.POST.get("stuid"))
    stuname=request.POST.get("stuname")
    stuprice=request.POST.get("stuprice")
    name1=Fruit.fu1.insert(stuid,stuname,stuprice)
    return HttpResponse(name1)
def amputate(request):#查询单个
      num=request.POST.get("number")
      fru=Fruit.fu1.filter(fruit=num)
      fruname=fru.fruname
      fruprice=fru.fruprice
      return HttpResponse( num+"---"+fruname+"---"+fruprice)
def cxqbquest(request):#查询全部
    mess=Fruit.fu1.change()
    return HttpResponse(mess)
def scdelete1(request):#删除
    num=int(request.POST.get("poot"))
    name=Fruit.fu1.scdelete(num)
    return HttpResponse(name)
def xgrevise1(request):#修改
     return render(request,'xg.html')
def xgrevise2(request):
    global num1
    num1 = int(request.POST.get("poot3"))
    list = Fruit.fu1.idnum()
    if num1 in list:
        return render(request,'xgrevise.html')
    else:
        return HttpResponse("您输入的序号不存在")
def xgrevise3(request):
    num2=request.POST.get("poot1")
    fru = Fruit.fu1.get(fruid=num1)
    if num1!=None:
        fru.fruname=num2
        fru.save()
        return HttpResponse("修改成功")
    else:
        return HttpResponse("没有改变元素")
def xgrevise4(request):
    num2 = request.POST.get("poot2")
    fru = Fruit.fu1.get(fruid=num1)
    if num2!=None:
        fru.fruprice=num2
        fru.save()
        return HttpResponse("修改成功")
    else:
        return HttpResponse("没有改变元素")