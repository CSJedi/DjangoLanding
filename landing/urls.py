from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.procedure_list, name='procedure_list'),
]
