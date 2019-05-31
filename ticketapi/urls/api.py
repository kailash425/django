from django.conf.urls import url
from  ticketapi.views import master
urlpatterns = [
    url("test",master.Test.as_view(), name="test"),
]