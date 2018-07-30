from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CurrentScavengerHuntView

urlpatterns = [
    path('', CurrentScavengerHuntView.as_view({'get': 'index', 'post': 'create'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
