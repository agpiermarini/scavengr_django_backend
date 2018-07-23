from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as drf_views
from .views import UserCreateView, UserScavengerHuntView, CustomAuthToken

urlpatterns = [
    path('', UserCreateView.as_view({'post': 'create'})),
    path('<id>/scavenger_hunts/', UserScavengerHuntView.as_view({'get': 'index'})),
    path('authenticate/', CustomAuthToken.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
