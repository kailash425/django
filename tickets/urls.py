from __future__ import unicode_literals
from django.conf.urls import url
from  tickets.views import login 
urlpatterns = [
    url("^",login, name="test"),
]