from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserApi.as_view()),
    path('users/<int:id>', views.UserApiDetails.as_view()),
    path('users/image/<int:id>', views.imageLoadUser)
]

urlpatterns = format_suffix_patterns(urlpatterns)
