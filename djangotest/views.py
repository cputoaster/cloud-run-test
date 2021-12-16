from django.contrib.auth.models import User
from rest_framework import viewsets

# ViewSets define the view behavior.
from djangotest.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer