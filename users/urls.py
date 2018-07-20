from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserView

urlpatterns = [
    re_path(r'^', UserView.as_view({'post': 'create'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
