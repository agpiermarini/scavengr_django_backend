from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ScavengerHuntView

urlpatterns = [
    path('', ScavengerHuntView.as_view({'get': 'index', 'post': 'create'})),
    path('<id>', ScavengerHuntView.as_view({'get': 'show', 'put': 'update', 'patch': 'update'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
