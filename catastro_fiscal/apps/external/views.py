from rest_framework_jwt.serializers import JSONWebTokenSerializer 
from rest_framework_jwt.views import ObtainJSONWebToken 


class CustomObtainJSONWebToken( ObtainJSONWebToken):
    serializer_class = JSONWebTokenSerializer