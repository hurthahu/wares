from django.conf.urls import url
from sqlapp import views

urlpatterns = [

    url(r"^selsect/$",views.selectlist),
    url(r'^selsect/cxquests/$',views.cxquest),
    url(r'^selsect/cxqbquest/$', views.cxqbquest),
    url(r'^selsect/cxquests/amputate/$', views.amputate),
    url(r'^selsect/scdelete/$',views.scdelete),
    url(r'^selsect/scdelete/scdelete1/$', views.scdelete1),
    url(r'^selsect/zjnature/$', views.zjnature),
    url(r'^selsect/zjnature/king/$', views.selsect),
    url(r'^selsect/xgrevise/$', views.xgrevise1),
    url(r'^selsect/xgrevise/xgrevise3/$', views.xgrevise2),
    url(r'^selsect/xgrevise/xgrevise3/xgrevise1/$', views.xgrevise3),
    url(r'^selsect/xgrevise/xgrevise3/xgrevise2/$', views.xgrevise4),

]
