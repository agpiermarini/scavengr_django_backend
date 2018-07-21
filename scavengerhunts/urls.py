from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ScavengerHuntView

urlpatterns = [
    path('', ScavengerHuntView.as_view({'post': 'create'})),
    path('<int:id>', ScavengerHuntView.as_view({'patch': 'update', 'put': 'update'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
