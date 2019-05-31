class BaseResponse(object):
    def __init__(self):
        self.response = {"success":False,"data":None,"errorMsg":None}
    
    def getBaseResponse(self):
        return self.response