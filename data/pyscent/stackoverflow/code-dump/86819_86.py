from django.contrib.auth.models import User
from rest_framework.generics import UpdateAPIView
from .serializers import UserSerializer

class UpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated
