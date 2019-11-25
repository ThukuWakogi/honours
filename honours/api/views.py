from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserProfileSerializer, ProjectSerializer, ProjectRatingSerializer
from .models import UserProfile, Project, ProjectRating
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #     users = User.objects.all()
    #     serializer = self.get_serializer(users, many=True)
    #     return Response(serializer.data)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRatingViewSet(viewsets.ModelViewSet):
    queryset = ProjectRating.objects.all()
    serializer_class = ProjectRatingSerializer
