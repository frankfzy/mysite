from django.conf.urls import url
from paltform import views

urlpatterns = [
    url(r'addProject', views.addProject),
    url(r'TwoProject', views.TwoProject),
    # url(r'getProject', views.getProject),
    url(r'getProject2', views.getProject2),
    url(r'updataproject', views.updataproject),
    url(r'deleteProject', views.deleteProject),
    url(r'addChildMoudle', views.addmodule)
]
