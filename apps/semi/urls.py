from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'create$', views.create),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^edit_user/(?P<id>\d+)$', views.edit_user),
    url(r'^profile$', views.profile),
    url(r'^profile/(?P<id>\d+)$', views.show_profile),
    url(r'^delete/(?P<id>\d+)$', views.delete)
]    