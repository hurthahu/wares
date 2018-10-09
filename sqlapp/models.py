from django.db import models
from django.http import HttpResponse

# Create your models here.
class Fruitmanager(models.Manager):
    def insert(self,stuid,stuname,stuprice):
        group=Fruit.fu1.idnum()
        if stuid in group:
            return ("您的序号重复无法添加成功")
        else:
            Fruit(fruid=stuid,fruname=stuname,fruprice=stuprice).save()
            return ("添加成功")

    def idnum(self):
      list=[]
      idlist=Fruit.fu1.all()
      for id in idlist:
         list.append(id.fruid)
      return list


    def change(self):
        sa = ""
        for fru in self.all():
          sa+=str(fru.fruid)+"-"+fru.fruname+"-"+fru.fruprice+"<br>"
        return sa

    def scdelete(self,stuid):
        list=Fruit.fu1.idnum()
        if stuid in list:
            fru2=Fruit.fu1.get(fruid=stuid)
            fru2.delete()
            return "删除成功"
        else:
            return ("您需要删除的序号不存在，删除失败")
    def xgrevise3(self,stuid):
        fru = Fruit.fu1.get(fruid=stuid)



class Fruit(models.Model):
    fu1=Fruitmanager()
    fruid=models.IntegerField(primary_key=True)
    fruname=models.CharField(max_length=50)
    fruprice=models.CharField(max_length=20)
