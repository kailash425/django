
from rest_framework.views import  APIView
from rest_framework.response import Response
from ticketapi.base_response import BaseResponse

class Test(APIView, BaseResponse):
    def __init__(self):
        BaseResponse.__init__(self)

    def get(self,request,**kwargds):
        response = self.getBaseResponse()
        
        return Response(response)
