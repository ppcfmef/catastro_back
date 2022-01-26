from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserProfileShortSerializer
from .models import User


class UserProfileShortView(APIView):
    queryset = User.objects.all()
    serializer_class = UserProfileShortSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
