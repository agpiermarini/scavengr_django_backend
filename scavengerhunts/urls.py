from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ScavengerHuntView

urlpatterns = [
    path('', ScavengerHuntView.as_view({'post': 'create'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
