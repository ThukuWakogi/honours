from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profiles', views.UserProfileViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'projectRatings', views.ProjectRatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.ObtainAuthTokenAndUserDetails.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
