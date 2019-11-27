from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
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
        print('in obtaining')
        response = super(ObtainAuthTokenAndUserDetails, self).post(request, *args, **kwargs)
        print('in obtaining 2')
        token = Token.objects.get(key=response.data['token'])
        print('in obtaining 3')
        user = User.objects.get(id=token.user_id)
        print('in obtaining 4')

        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRatingViewSet(viewsets.ModelViewSet):
    queryset = ProjectRating.objects.all()
    serializer_class = ProjectRatingSerializer
