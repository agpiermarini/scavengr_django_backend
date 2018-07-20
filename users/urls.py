from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as drf_views
from .views import UserView

urlpatterns = [
    path('', UserView.as_view({'post': 'create'})),
    path('authenticate/', drf_views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
