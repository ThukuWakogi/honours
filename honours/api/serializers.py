from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, Project, ProjectRating


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = dict(
            password={
                'write_only': True,
                'required': True,
                'allow_null': False
            },
            email={
                'required': True,
                'allow_null': False
            }
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        extra_kwargs = dict(
            profile_pic={
                'required': True,
                'allow_null': False
            },
            user={
                'required': True,
                'allow_null': False
            }
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = dict(
            title={
                'required': True,
                'allow_null': False
            },
            landing_page_image={
                'required': True,
                'allow_null': False
            },
            description={
                'required': True,
                'allow_null': False
            },
            link={
                'required': True,
                'allow_null': False
            },
            user={
                'required': False,
            },
            date_added={
                'required': True,
                'allow_null': False,
                'read_only': True,
            }
        )


class ProjectRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRating
        fields = '__all__'
        extra_kwargs = dict(
            user={
                'required': True,
                'allow_null': False
            },
            project={
                'required': True,
                'allow_null': False
            },
            design={
                'required': True,
                'allow_null': False
            },
            usability={
                'required': True,
                'allow_null': False
            },
            content={
                'required': True,
                'allow_null': False
            },
            date_added={
                'required': True,
                'allow_null': False,
                'write_only': True,
            }
        )
