from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import UsersView

urlpatterns = [
    path('api/v1/users/', UsersView.as_view({'get': 'create'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)
