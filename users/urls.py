from django.urls import include, path

from .views import ListUsersAPIView

app_name = 'users'

urlpatterns = [
    path('user-accounts/list/', ListUsersAPIView.as_view()),
]
