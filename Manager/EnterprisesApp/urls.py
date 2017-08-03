from django.conf.urls import url
from . import views

urlpatterns = [
    #/enterprises/
    url(r'^$', views.all_enterprises, name='all_enterprises'),
    #/enterprises/id   ex: /enterprises/2 -> details about enterprise with id 2
    url(r'^(?P<enterprise_id>[0-9]+)/$', views.enterprise_details, name="enterprise_details"),


]
