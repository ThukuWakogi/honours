from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import UserSerializer, UserProfileSerializer, ProjectSerializer, ProjectRatingSerializer
from .models import UserProfile, Project, ProjectRating
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)

        return Response(
            {
                'token': token.key,
                'user': serializer.data,
                'created': created
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class ObtainAuthTokenAndUserDetails(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(ObtainAuthTokenAndUserDetails, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)

        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })


class UserDetailsFromToken(RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        return Response(dict(
            user={
                'id': request.user.id,
                'username': request.user.username,
                'email': request.user.email
            }
        ))


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request, *args, **kwargs):
        request.data.update({'user': request.user.id})
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        projects = Project.objects.all().order_by('-date_added')
        serializer = ProjectSerializer(projects, many=True)
        projects_and_users = []

        for project in serializer.data:
            user = User.objects.get(id=dict(project)['user'])
            projects_and_users.append({
                'id': dict(project)['id'],
                'title': dict(project)['title'],
                'landing_page_image': dict(project)['landing_page_image'],
                'description': dict(project)['description'],
                'link': dict(project)['link'],
                'date_added': dict(project)['date_added'],
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email
                }
            })

        return Response(projects_and_users)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Project.objects.all()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectSerializer(project)
        user = User.objects.get(id=serializer.data['user'])

        return Response({
            'id': serializer.data['id'],
            'title': serializer.data['title'],
            'landing_page_image': serializer.data['landing_page_image'],
            'description': serializer.data['description'],
            'link': serializer.data['link'],
            'date_added': serializer.data['date_added'],
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })


class ProjectRatingViewSet(viewsets.ModelViewSet):
    queryset = ProjectRating.objects.all()
    serializer_class = ProjectRatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
